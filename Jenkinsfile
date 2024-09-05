pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    bat 'C:\\Python39\\python.exe -m venv venv'
                    bat 'call venv\\Scripts\\activate && pip install --upgrade pip'
                    bat 'pip install --upgrade virtualenv'
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    bat 'call venv\\Scripts\\activate && pytest test\\test_add_group.py'
                }
            }
        }
    }
}