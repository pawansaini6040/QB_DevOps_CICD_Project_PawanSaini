pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "doc201/flask-app"
        TAG = "${BUILD_NUMBER}"
        KUBECONFIG = "/var/lib/jenkins/.kube/config"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/Dev664/db12cicd_updated'
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                  # docker build -t $DOCKER_IMAGE:$TAG .
                    docker build --no-cache -t $DOCKER_IMAGE:$TAG .
                '''
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $DOCKER_IMAGE:$TAG
                    '''
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                sh '''
                    if kubectl get deployment flask-deployment >/dev/null 2>&1
                    then
                        echo "Deployment exists. Updating image..."

                        kubectl set image deployment/flask-deployment \
                        flask=$DOCKER_IMAGE:$TAG

                    else
                        echo "First deployment. Creating resources..."

                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml

                        kubectl set image deployment/flask-deployment \
                        flask=$DOCKER_IMAGE:$TAG
                    fi

                    kubectl rollout status deployment/flask-deployment
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
