pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                echo 'Setting console encoding to UTF-8'
                bat 'chcp 65001'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Creating virtual environment'
                bat 'python -m venv venv'
                echo 'Activating virtual environment and installing dependencies'
                bat '.\\venv\\Scripts\\activate && python -m pip install --upgrade pip && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    echo 'Running test_add_group.py with pytest'
                    bat '.\\venv\\Scripts\\activate && pytest -v D:\\QA\\AUTO\\python_training_2\\test\\test_add_group.py'
                }
            }
        }
    }
    post {
        always {
            echo 'Deactivating virtual environment'
            bat '.\\venv\\Scripts\\deactivate'
        }
    }
}

Find More