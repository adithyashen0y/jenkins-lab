pipeline {
    agent any

    environment {
        IMAGE = 'hello-app'
    }

    stages {
        stage('Info') {
            steps {
                echo "Building ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                sh 'python3 --version && docker --version'
            }
        }

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest tests --junitxml=reports/junit.xml
                '''
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER .'
            }
        }

        stage('Deploy') {
            environment {
                APP_SECRET = credentials('app-secret')
            }
            steps {
                sh 'docker run -d --name hello-app -p 8081:5000 -e APP_SECRET -e APP_VERSION=$BUILD_NUMBER $IMAGE:$BUILD_NUMBER'
            }
        }

        stage('Smoke test') {
            steps {
                sh 'curl -fsS http://localhost:8081/health'
            }
        }
    }

    post {
        always {
            junit 'report/*.xml'
        }
        success {
            echo 'Deployed! Open http://<VM-IP>:8081'
        }
        failure {
            echo 'Build failed. Read the log above, find the first real error.'
        }
    }
}
