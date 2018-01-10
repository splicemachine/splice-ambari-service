# splice-ambari-service
An Apache Ambari Service For Splice Machine

#### Steps to deploy to HDP Virtual Machine.

1) Download HDP Sandbox for VirtualBox. https://hortonworks.com/tutorial/sandbox-deployment-and-install-guide/section/1/
2) Start Virtual Machine.
3) Log into virtual machine.

```
ssh root@127.0.0.1 -p2222
initial password hadoop
```

4) Make sure you have FPM installed properly for your environment.

http://fpm.readthedocs.io/en/latest/

5) Get latest ambari service branch to generate the RPM and restart Ambari Server.

```
git clone git@github.com:splicemachine/splice-ambari-service.git
cd splice-ambari-service
./build.sh
rpm -Uvh target/SOME_RPM_FILE_WITH_NO_ARCH
ambari-server restart 
```

6) Access the Ambari server UI.

```
http://127.0.0.1:8080/#/main/dashboard/metrics
```
7) Follow the steps to install a servive.

<img src="docs/Add_Service.jpeg" alt="Add Service" width="200" height="200">
<img src="docs/Add_Service_Wizard.jpeg" alt="Add Service Wizard" width="400" height="200">
<img src="docs/Install_Start_And_Test.jpeg" alt="Add Service Install Start and Test" width="400" height="200">
<img src="docs/Splice_Machine_Installed.jpeg" alt="Splice Machine Installed" width="100" height="200">
