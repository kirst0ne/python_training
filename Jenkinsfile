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
                    call .\\venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    echo 'Running specific test with pytest'
                    bat '''
                        call .\\venv\\Scripts\\activate
                        pytest D:\\QA\\AUTO\\python_training_2\\test\\test_add_group.py -v --junitxml=results.xml --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Publishing JUnit test results'
                junit 'results.xml'
                echo 'Generating Allure report'
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Deactivating virtual environment'
            bat 'call .\\venv\\Scripts\\deactivate'
        }
    }
}
