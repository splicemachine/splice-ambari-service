import os
import shutil
import sys
import sys
from resource_management import *

reload(sys)
sys.setdefaultencoding('utf8')

class SpliceInstall(Script):
  def install(self, env):
    import params
    env.set_params(params)
    print(params)
    print 'Install the client';
    dir = '/var/lib/splicemachine'
    if os.path.exists(dir):
      shutil.rmtree(dir)
    os.makedirs(dir)

    #os.system("wget -O /var/lib/splicemachine/db-client-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-client/2.5.0.1735/db-client-2.5.0.1735.jar")
    #os.system("wget -O /var/lib/splicemachine/db-drda-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-drda/2.5.0.1735/db-drda-2.5.0.1735.jar")
    #os.system("wget -O /var/lib/splicemachine/db-shared-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-shared/2.5.0.1735/db-shared-2.5.0.1735.jar")
    #os.system("wget -O /var/lib/splicemachine/db-tools-i18n-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-tools-i18n/2.5.0.1735/db-tools-i18n-2.5.0.1735.jar")
    #os.system("wget -O /var/lib/splicemachine/db-tools-ij-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-tools-ij/2.5.0.1735/db-tools-ij-2.5.0.1735.jar")
    #os.system("wget -O /var/lib/splicemachine/utilities-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/utilities/2.5.0.1735/utilities-2.5.0.1735.jar")
    #os.system("wget -O /var/lib/splicemachine/memory-0.8.4.jar https://repo.maven.apache.org/maven2/com/yahoo/datasketches/memory/0.8.4/memory-0.8.4.jar")
    #os.system("wget -O /var/lib/splicemachine/sketches-core-0.8.4.jar https://repo.maven.apache.org/maven2/com/yahoo/datasketches/sketches-core/0.8.4/sketches-core-0.8.4.jar")
    #os.system("wget -O /var/lib/splicemachine/hppc-0.5.2.jar https://repo.maven.apache.org/maven2/com/carrotsearch/hppc/0.5.2/hppc-0.5.2.jar")
    #os.system("wget -O /var/lib/splicemachine/opencsv-2.3.jar https://repo.maven.apache.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar")
    # HDP Specific Artifacts
    os.system("cp /root/full/splice_access_api-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/splice_encoding-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/splice_machine-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/splice_protocol-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/splice_si_api-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/pipeline_api-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/splice_timestamp_api-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/db-client-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/db-drda-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/db-engine-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/db-shared-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/db-tools-i18n-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/utilities-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/memory-0.8.4.jar /var/lib/splicemachine/")
    os.system("cp /root/full/sketches-core-0.8.4.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hppc-0.5.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/opencsv-2.3.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hbase_pipeline-hdp2.6.3-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/opencsv-2.3.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hbase_storage-hdp2.6.3-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hbase_sql-hdp2.6.3-2.7.0.1802-SNAPSHOT.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-network-yarn_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-network-shuffle_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-network-common_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-core_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-catalyst_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-sql_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-unsafe_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-tags_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/spark-launcher_2.11-2.2.0.2.6.3.0-235.jar /var/lib/splicemachine/")
    os.system("cp /root/full/concurrentlinkedhashmap-lru-1.4.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/scala-library-2.11.8.jar /var/lib/splicemachine/")
    os.system("cp /root/full/kryo-shaded-3.0.3.jar /var/lib/splicemachine/")
    os.system("cp /root/full/kryo-serializers-0.38.jar /var/lib/splicemachine/")
    os.system("cp /root/full/lucene-core-4.3.1.jar /var/lib/splicemachine/")
    os.system("cp /root/full/minlog-1.3.0.jar /var/lib/splicemachine/")
    os.system("cp /root/full/akka-remote_2.11-2.4.8.jar /var/lib/splicemachine/")
    os.system("cp /root/full/chill_2.11-0.8.0.jar /var/lib/splicemachine/")
    os.system("cp /root/full/json4s-jackson_2.11-3.2.11.jar /var/lib/splicemachine/")
    os.system("cp /root/full/json4s-ast_2.11-3.2.11.jar /var/lib/splicemachine/")
    os.system("cp /root/full/json4s-core_2.11-3.2.11.jar /var/lib/splicemachine/")
    os.system("cp /root/full/scala-xml_2.11-1.0.1.jar /var/lib/splicemachine/")
    os.system("cp /root/full/javax.servlet-api-3.1.0.jar /var/lib/splicemachine/")
    os.system("cp /root/full/metrics-json-3.1.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/lz4-1.3.0.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jackson-module-scala_2.11-2.6.5.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jackson-core-2.6.5.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jackson-annotations-2.6.5.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jackson-databind-2.6.5.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jackson-module-paranamer-2.6.5.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jersey-server-2.22.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jersey-client-2.22.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jersey-common-2.22.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jersey-guava-2.22.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jersey-container-servlet-core-2.22.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/jersey-server-2.22.2.jar /var/lib/splicemachine/")
    os.system("cp /root/full/javax.ws.rs-api-2.0.1.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hk2-api-2.4.0-b34.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hk2-utils-2.4.0-b34.jar /var/lib/splicemachine/")
    os.system("cp /root/full/hk2-locator-2.4.0-b34.jar /var/lib/splicemachine/")
    os.system("cp /root/full/xbean-asm5-shaded-4.4.jar /var/lib/splicemachine/")
    os.system("cp /root/full/scala-library-2.11.8.jar /var/lib/splicemachine/")
    os.system("cp /root/full/kryo-shaded-3.0.3.jar /var/lib/splicemachine/")

  def configure(self, env):
    print 'Configure the client';
  def somethingcustom(self, env):
    print 'Something custom';

if __name__ == "__main__":
  SpliceInstall().execute()