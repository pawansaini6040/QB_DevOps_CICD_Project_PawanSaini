#  CI/CD setup with Jenkins 

In this LAB we will perform the below tasks :
1.  Setup a k8s cluster with one control plane and one worker node .
2.  Install and configure Jenkins on a seperate Ec2 instance and make it work as jenkin server .
3.  Create all the required defination files and programs 
4.  Stup the CI/CD pipeline with jenkins 
5.  Test the pipe line .

## Setup a k8s cluster with one control plane and one worker node .


## Install and configure Jenkins node 

Official Documentation page :
https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos

### We are setting up Jenkins on Amazon Linux Ec2 

craete an Ec2 instance with the below specifications 

use the same Security group as k8s cluster else open the below ports on your SG 
22  SSH
8080  Jenkins UI 
30000–32767 NodePort (for K8s apps)

instance Type : t2.medium Storage : Minimum: 20 GB


Install Java 
```
yum install java-17-amazon-corretto -y 
```
Install Jenkins 
```
wget -O /etc/yum.repos.d/jenkins.repo \ 
https://pkg.jenkins.io/redhat-stable/jenkins.repo

rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key 
yum install jenkins -y 
```
Start Jenkins 
```
sudo systemctl start jenkins 
sudo systemctl enable jenkins 
```
Access The GUI : 
```
http://<jenkins-ip>:8080 
```
once you open the url for UI it will ask  to unlock 
To Unlock for the first time  run the below command in Jenkins server and the o/p you will get and o/p
enter it to teh UI page 
```
cat /var/lib/jenkins/secrets/initialAdminPassword 
```

### setup Docker in the jenkins server 

In the jenkins server  setup docer and kubectl
```
dnf install git docker -y 

systemctl start docker 
systemctl enable docker 

usermod -aG docker jenkins 

systemctl restart jenkins 
```

Install kubectl  
```
curl -LO https://dl.k8s.io/release/v1.30.0/bin/linux/amd64/kubectl 

chmod +x kubectl 

mv kubectl /usr/local/bin/
```

### Connect Jenkins to  Kubernetes Cluster

Copy kubeconfig from control plane to jenkins server : 

On control plane: 
```

cat ~/.kube/config
```
On Jenkins server Paste config : 
```
mkdir -p /var/lib/jenkins/.kube 
vi /var/lib/jenkins/.kube/config 
```
Fix permissions: 
```
chown -R jenkins:jenkins /var/lib/jenkins/.kube 
```
Test if it is working or not : 
```
kubectl get nodes 

sudo -u jenkins kubectl get nodes 
````
### Setup Docker Registry login from jenkins server 
As we will use Docker Hub , from setup the login from jenkins server to docker hub 
docker login 
provid ecredentails 

## craete all the required files and push to a github repo 
cicdtest1
app.py
Dockerfile 
requirements.txt

Push all the files to github 
Create Kubernetes Deployment and service defination files
deployment.yaml
service.yaml

## Setup Jenkins Credentials 

Open Jenkins UI  : http://<jenkins-ec2-ip>:8080 
login as admin 

Go to Credentials  from settings  
  Select Store 
  Add Credentials 
  Username with password

 ## Jenkins Pipeline Setup 

### Install Required Plugins 

Verify and if not required Install: 
Pipeline  (this should already available , just search ) 
Git  (this should already available , just search ) 
Docker Pipeline  (This need to install) 

### Create Pipeline Job 

### create the pipeline config file / jenkins file 

### Run the build 


## Test the CI/CD workflow 

### Modify the app.py from gitbash
push it 

### setuip Setup Webhook for auto build and deploy 



