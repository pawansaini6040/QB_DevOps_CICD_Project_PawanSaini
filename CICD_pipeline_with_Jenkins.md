# 🚀 End-to-End CI/CD Pipeline using Jenkins, Docker, GitHub & Kubernetes

> A complete hands-on DevOps project demonstrating Continuous Integration and Continuous Deployment (CI/CD) using Jenkins, Docker Hub, GitHub, and Kubernetes.

**Created by Debdip Ghosh**

---

# 📖 Project Overview

This project demonstrates how a code change pushed to GitHub automatically:

- Triggers Jenkins
- Builds a Docker image
- Pushes the image to Docker Hub
- Deploys the latest version to Kubernetes
- Makes the updated application available to users

---

# 🏗️ Architecture Diagram

```text
+-------------+
| Developer   |
+-------------+
       |
       | Git Push
       v
+---------------------+
| GitHub Repository   |
+---------------------+
       |
       | Webhook
       v
+---------------------+
| Jenkins Pipeline    |
+---------------------+
       |
       +---------------------+
       |                     |
       v                     |
 Build & Test                |
       |                     |
       v                     |
 Build Docker Image          |
       |                     |
       v                     |
+---------------------+      |
| Docker Hub          |<-----+
+---------------------+
       |
       | Pull Image
       v
+---------------------+
| Kubernetes Cluster  |
+---------------------+
       |
       v
+---------------------+
| Application Running |
+---------------------+
```

---

# 🔄 CI/CD Workflow

```text
Developer
    │
    ▼
GitHub Push
    │
    ▼
Webhook Trigger
    │
    ▼
Jenkins Pipeline
    │
    ├── Clone Code
    ├── Build Application
    ├── Run Tests
    ├── Build Docker Image
    ├── Push Image
    └── Deploy to Kubernetes
    │
    ▼
Docker Hub
    │
    ▼
Kubernetes Cluster
    │
    ▼
Updated Application
```

---

# 🛠️ Technology Stack

| Component | Purpose |
|------------|----------|
| GitHub | Source Code Management |
| Jenkins | CI/CD Automation |
| Docker | Containerization |
| Docker Hub | Image Registry |
| Kubernetes | Container Orchestration |
| Flask | Demo Application |
| AWS EC2 | Jenkins Hosting |

---

# 📋 Prerequisites

- AWS EC2 Instance (Amazon Linux)
- Kubernetes Cluster
- GitHub Account
- Docker Hub Account
- Internet Connectivity
- Security Group allowing:
  - TCP 8080 (Jenkins)
  - TCP 22 (SSH)

---

# ⚙️ Phase 1 – Jenkins Setup

## Install Java

```bash
sudo yum install java-17-amazon-corretto -y
```

## Install Jenkins

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

sudo yum install jenkins -y
```

## Start Jenkins

```bash
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

## Access Jenkins

```text
http://<JENKINS-IP>:8080
```

Retrieve Admin Password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

# 🐳 Phase 2 – Docker Installation

```bash
sudo dnf install git docker -y

sudo systemctl start docker
sudo systemctl enable docker

sudo usermod -aG docker jenkins

sudo systemctl restart jenkins
```

Verify:

```bash
docker ps
```

---

# ☸️ Phase 3 – Kubernetes Integration

Install kubectl:

```bash
curl -LO https://dl.k8s.io/release/v1.30.0/bin/linux/amd64/kubectl

chmod +x kubectl

sudo mv kubectl /usr/local/bin/
```

Copy kubeconfig from Kubernetes Control Plane to Jenkins:

```bash
mkdir -p /var/lib/jenkins/.kube

vi /var/lib/jenkins/.kube/config
```

Set permissions:

```bash
sudo chown -R jenkins:jenkins /var/lib/jenkins/.kube
```

Verify:

```bash
sudo -u jenkins kubectl get nodes
```

---

# 📦 Phase 4 – Application Setup

## Flask Application

### app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Version 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### requirements.txt

```text
flask
```

### Dockerfile

```dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

# 🌐 Phase 5 – GitHub Setup

Initialize Repository:

```bash
git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin https://github.com/<username>/<repo>.git

git push -u origin main
```

Verify Remote:

```bash
git remote -v
```

Change Remote:

```bash
git remote set-url origin https://github.com/<username>/<new-repo>.git
```

---

# ☸️ Phase 6 – Kubernetes Deployment

## deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-deployment
spec:
  replicas: 2
```

## service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  type: NodePort
```

Deploy:

```bash
kubectl apply -f deployment.yaml

kubectl apply -f service.yaml
```

---

# 🔐 Phase 7 – Jenkins Credentials

## Docker Hub Credentials

Credential ID:

```text
dockerhub-creds
```

## GitHub Credentials

Credential ID:

```text
github-creds
```

Use a GitHub Personal Access Token (PAT).

---

# 🔌 Required Jenkins Plugins

- Pipeline
- Git
- Docker Pipeline
- GitHub Integration Plugin

---

# 🧪 Jenkins Pipeline

```groovy
pipeline {

    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhub/flask-app"
        TAG = "${BUILD_NUMBER}"
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

    stages {

        stage('Clone Code') {
            steps {
                git credentialsId: 'github-creds',
                url: 'https://github.com/repository.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$TAG .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE:$TAG'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                kubectl set image deployment/flask-deployment \
                flask=$DOCKER_IMAGE:$TAG
                '''
            }
        }
    }
}
```

---

# 🔔 GitHub Webhook Configuration

Webhook URL:

```text
http://<JENKINS-IP>:8080/github-webhook/
```

GitHub:

```text
Repository
 └── Settings
      └── Webhooks
           └── Add Webhook
```

Enable:

```text
Push Event
```

Jenkins Job:

```text
GitHub hook trigger for GITScm polling
```

---

# ✅ Verification Commands

```bash
kubectl get pods -w

kubectl get svc

kubectl get deployments

docker images

git remote -v
```

---

# 🚨 Troubleshooting

## Jenkins Logs

```bash
sudo journalctl -u jenkins.service -n 100 --no-pager
```

## Docker Access

```bash
docker ps
```

## Kubernetes Access

```bash
sudo -u jenkins kubectl get nodes
```

---

# 🎯 Expected Result

After pushing code to GitHub:

```text
GitHub Push
    ↓
Webhook Trigger
    ↓
Jenkins Build
    ↓
Docker Image Build
    ↓
Docker Hub Push
    ↓
Kubernetes Deployment
    ↓
Application Updated
```

The entire software delivery process becomes fully automated.

---

# 👨‍💻 Author

**Debdip Ghosh**

DevOps Engineer 
