pipeline {
    agent any
    environment {
        PYTHONPATH = "${WORKSPACE}"
    }
    stages {
        stage('Setup') {
            steps {
                bat 'python --version'
                bat 'pip install flask'
            }
        }
        stage('Lint') {
            steps {
                bat 'pip install flake8'
                bat 'flake8 app.py'
            }
        }
        stage('Run') {
            steps {
                bat 'python app.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
