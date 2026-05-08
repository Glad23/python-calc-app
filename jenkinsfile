pipeline {
    agent any
    
    stages {
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying app'
            }
        }
    }
}