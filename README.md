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


![alt text](docs/Add_Service.jpeg "Add Service")

![alt text](docs/Add_Service_Wizard.jpeg "Add Service Wizard")

![alt text](docs/Install_Start_And_Test.jpeg "Add Service Install Start and Test")

![alt text](docs/Splice_Machine_Installed.jpeg "Splice Machine Installed")
