#!/usr/bin/env ambari-python-wrap
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import imp
import math
import os
import re
import socket
import traceback

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STACKS_DIR = os.path.join(SCRIPT_DIR, '../../../../../stacks/')
PARENT_FILE = os.path.join(STACKS_DIR, 'service_advisor.py')

try:
  with open(PARENT_FILE, 'rb') as fp:
    service_advisor = imp.load_module('service_advisor', fp, PARENT_FILE, ('.py', 'rb', imp.PY_SOURCE))
except Exception as e:
  traceback.print_exc()
  print "Failed to load parent"

class HDP26SPLICEMACHINEServiceAdvisor(service_advisor.ServiceAdvisor):

  def __init__(self, *args, **kwargs):
    self.as_super = super(HDP26SPLICEMACHINEServiceAdvisor, self)
    self.as_super.__init__(*args, **kwargs)

  def colocateService(self, hostsComponentsMap, serviceComponents):
    pass

  def getServiceConfigurationRecommendations(self, configurations, clusterData, services, hosts):

    # Update HDFS properties in core-site
    if "core-site" in services["configurations"]:
      core_site = services["configurations"]["core-site"]["properties"]
      putCoreSiteProperty = self.putProperty(configurations, "core-site", services)

      for property, desired_value in self.getCoreSiteDesiredValues().iteritems():
        if property not in core_site or core_site[property] != desired_value:
          putCoreSiteProperty(property, desired_value)

    # Update HBase Classpath
    if "hbase-env" in services["configurations"]:
        hbase_env = services["configurations"]["hbase-env"]["properties"]
        if "content" in hbase_env:
            content = hbase_env["content"]
            SPLICE_PATH = "export HBASE_CLASSPATH=${HBASE_CLASSPATH}:/usr/lib/splicemachine/*"
            if "splicemachine" not in content:
                SPLICE_PATH = "#Add pxf-hbase.jar to HBASE_CLASSPATH\n" + SPLICE_PATH
                content = "\n\n".join((content, SPLICE_PATH))
                putHbaseEnvProperty = self.putProperty(configurations, "hbase-env", services)
                putHbaseEnvProperty("content", content)


  def getServiceConfigurationsValidationItems(self, configurations, recommendedDefaults, services, hosts):

    # validate recommended properties in core-site
    siteName = "core-site"
    method = self.validateCoreSiteConfigurations
    items = self.validateConfigurationsForSite(configurations, recommendedDefaults, services, hosts, siteName, method)

    siteName = "hdfs-site"
    method = self.validateHDFSSiteConfigurations
    resultItems = self.validateConfigurationsForSite(configurations, recommendedDefaults, services, hosts, siteName, method)
    items.extend(resultItems)

    siteName = "hbase-site"
    method = self.validateHBaseSiteConfigurations
    resultItems = self.validateConfigurationsForSite(configurations, recommendedDefaults, services, hosts, siteName, method)
    items.extend(resultItems)

    return items


  def validateCoreSiteConfigurations(self, properties, recommendedDefaults, configurations, services, hosts):
    core_site = properties
    validationItems = []
    for property, desired_value in self.getCoreSiteDesiredValues().iteritems():
      if property not in core_site or core_site[property] != desired_value:
        message = "Splice Machine requires this property to be set to the recommended value of " + desired_value
        validationItems.append({"config-name": property, "item": self.getWarnItem(message)})
    return self.toConfigurationValidationProblems(validationItems, "core-site")

  def validateHDFSSiteConfigurations(self, properties, recommendedDefaults, configurations, services, hosts):
      hdfs_site = properties
      validationItems = []
      for property, desired_value in self.getHDFSSiteDesiredValues().iteritems():
          if property not in hdfs_site or hdfs_site[property] != desired_value:
              message = "Splice Machine requires this property to be set to the recommended value of " + desired_value
              validationItems.append({"config-name": property, "item": self.getWarnItem(message)})
      return self.toConfigurationValidationProblems(validationItems, "hdfs-site")

  def validateHBaseSiteConfigurations(self, properties, recommendedDefaults, configurations, services, hosts):
      hbase_site = properties
      validationItems = []
      for property, desired_value in self.getHBaseSiteDesiredValues().iteritems():
          if property not in hbase_site or hbase_site[property] != desired_value:
              message = "Splice Machine requires this property to be set to the recommended value of " + desired_value
              validationItems.append({"config-name": property, "item": self.getWarnItem(message)})
      return self.toConfigurationValidationProblems(validationItems, "hbase-site")

  def getCoreSiteDesiredValues(self):
    core_site_desired_values = {
        "ipc.server.listen.queue.size" : "3300"
    }
    return core_site_desired_values

  def getHDFSSiteDesiredValues(self):
    hdfs_site_desired_values = {
        "dfs.datanode.handler.count" : "20",
        "dfs.client.read.shortcircuit.buffer.size" : "131072",

    }
    return hdfs_site_desired_values

  def getHBaseSiteDesiredValues(self):
    hbase_site_desired_values = {
        "hbase.regionserver.global.memstore.size" : "0.25",
        "hfile.block.cache.size" : "0.25",
        "hbase.regionserver.handler.count" : "200",
        "hbase.client.scanner.caching" : "1000",
        "hbase.hstore.blockingStoreFiles" : "20",
        "hbase.hstore.compactionThreshold" : "5",
        "hbase.balancer.period" : "60000",
        "hbase.client.ipc.pool.size" : "10",
        "hbase.client.max.perregion.tasks" : "100",
        "hbase.coprocessor.regionserver.classes" : "com.splicemachine.hbase.RegionServerLifecycleObserver",
        "hbase.hstore.compaction.max.size" : "260046848",
        "hbase.hstore.compaction.min.size" : "16777216",
        "hbase.hstore.compaction.min" : "5",
        "hbase.hstore.defaultengine.compactionpolicy" : "com.splicemachine.compactions.SpliceDefaultCompactionPolicy",
        "hbase.hstore.defaultengine.compactor" : "com.splicemachine.compactions.SpliceDefaultCompactor",
        "hbase.coprocessor.region.classes" : "com.splicemachine.hbase.MemstoreAwareObserver,com.splicemachine.derby.hbase.SpliceIndexObserver,com.splicemachine.derby.hbase.SpliceIndexEndpoint,com.splicemachine.hbase.RegionSizeEndpoint,com.splicemachine.si.data.hbase.coprocessor.TxnLifecycleEndpoint,com.splicemachine.si.data.hbase.coprocessor.SIObserver,com.splicemachine.hbase.BackupEndpointObserver",
        "hbase.htable.threads.max" : "96",
        "hbase.ipc.warn.response.size" : "-1",
        "hbase.ipc.warn.response.time" : "-1",
        "hbase.master.loadbalance.bytable" : "true",
        "hbase.htable.threads.max" : "96",
        "hbase.regions.slop" : "0.01",
        "hbase.regionserver.global.memstore.size.lower.limit" : "0.9",
        "hbase.regionserver.lease.period" : "1200000",
        "hbase.regionserver.maxlogs" : "48",
        "hbase.regionserver.thread.compaction.large" : "1",
        "hbase.regionserver.thread.compaction.small" : "4",
        "hbase.regionserver.wal.enablecompression" : "true",
        "hbase.rowlock.wait.duration" : "0",
        "hbase.splitlog.manager.timeout" : "3000",
        "hbase.status.multicast.port" : "16100",
        "hbase.wal.disruptor.batch" : "true",
        "hbase.wal.provider" : "multiwal",
        "hbase.wal.regiongrouping.numgroups" : "16",
        "hbase.zookeeper.property.tickTime" : "6000",
        "hfile.block.bloom.cacheonwrite" : "TRUE",
        "io.storefile.bloom.error.rate" : "0.005",
        "splice.authentication.native.algorithm" : "SHA-512",
        "splice.authentication" : "NATIVE",
        "splice.client.numConnections" : "1",
        "splice.client.write.maxDependentWrites" : "60000",
        "splice.client.write.maxIndependentWrites" : "60000",
        "splice.compression" : "snappy",
        "splice.marshal.kryoPoolSize" : "1100",
        "splice.olap_server.clientWaitTime" : "900000",
        "splice.ring.bufferSize" : "131072",
        "splice.splitBlockSize" : "67108864",
        "splice.timestamp_server.clientWaitTime" : "120000",
        "splice.txn.activeTxns.cacheSize" : "10240",
        "splice.txn.completedTxns.concurrency" : "128",
        "splice.txn.concurrencyLevel" : "4096"
    }
    return hbase_site_desired_values
