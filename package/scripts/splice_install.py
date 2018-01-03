import sys
import grp
import os
import pwd
import sys
import shutil

from resource_management import *

reload(sys)
sys.setdefaultencoding('utf8')

class SpliceInstall(Script):
  def install(self, env):
    import params
    env.set_params(params)
    print 'Install the client';
    dir = '/var/lib/splicemachine'
    if os.path.exists(dir):
      shutil.rmtree(dir)
    os.makedirs(dir)
    os.system("wget -O /var/lib/splicemachine/db-client-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-client/2.5.0.1735/db-client-2.5.0.1735.jar")
    os.system("wget -O /var/lib/splicemachine/db-drda-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-drda/2.5.0.1735/db-drda-2.5.0.1735.jar")
    os.system("wget -O /var/lib/splicemachine/db-shared-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-shared/2.5.0.1735/db-shared-2.5.0.1735.jar")
    os.system("wget -O /var/lib/splicemachine/db-tools-i18n-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-tools-i18n/2.5.0.1735/db-tools-i18n-2.5.0.1735.jar")
    os.system("wget -O /var/lib/splicemachine/db-tools-ij-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/db-tools-ij/2.5.0.1735/db-tools-ij-2.5.0.1735.jar")
    os.system("wget -O /var/lib/splicemachine/utilities-2.5.0.1735.jar http://repository.splicemachine.com/nexus/content/repositories/releases/com/splicemachine/utilities/2.5.0.1735/utilities-2.5.0.1735.jar")
    os.system("wget -O /var/lib/splicemachine/memory-0.8.4.jar https://repo.maven.apache.org/maven2/com/yahoo/datasketches/memory/0.8.4/memory-0.8.4.jar")
    os.system("wget -O /var/lib/splicemachine/sketches-core-0.8.4.jar https://repo.maven.apache.org/maven2/com/yahoo/datasketches/sketches-core/0.8.4/sketches-core-0.8.4.jar")
    os.system("wget -O /var/lib/splicemachine/hppc-0.5.2.jar https://repo.maven.apache.org/maven2/com/carrotsearch/hppc/0.5.2/hppc-0.5.2.jar")
    os.system("wget -O /var/lib/splicemachine/opencsv-2.3.jar https://repo.maven.apache.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar")
    # HDP Specific Artifacts

  def configure(self, env):
    print 'Configure the client';
  def somethingcustom(self, env):
    print 'Something custom';

if __name__ == "__main__":
  SpliceInstall().execute()