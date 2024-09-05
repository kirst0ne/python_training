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
                bat '''
                    .\\venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    echo 'Running tests with pytest'
                    bat '''
                        .\\venv\\Scripts\\activate
                        pytest -v --junitxml=results.xml --alluredir=allure-results D:\\QA\\AUTO\\python_training_2\\test
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Publishing JUnit test results'
            junit 'results.xml'

            echo 'Generating Allure report'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']], commandline: 'allure'

            echo 'Deactivating virtual environment'
            bat '.\\venv\\Scripts\\deactivate'
        }
    }
}
