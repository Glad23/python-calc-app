pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm 
            }
        }
        stage('Setup Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }
        stage('Install') {   
            steps {
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying app'
            }
        }
    }
    
post {
    always {
        echo 'pipeline execution completed.'
    }
    Success {
        echo 'SUCCESS'
    }
    Failure {
        echo 'FAILED'
    }
}
}
