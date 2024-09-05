pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Python39'
        PATH = "${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    echo 'Setting console encoding to UTF-8'
                    bat 'chcp 65001'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Creating virtual environment'
                    bat 'python -m venv venv'
                    
                    echo 'Activating virtual environment and installing dependencies'
                    bat '.\\venv\\Scripts\\activate && pip install --upgrade pip setuptools wheel && pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    script {
                        echo 'Running test_add_group.py'
                        bat '.\\venv\\Scripts\\activate && python -m unittest test_add_group.py'
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                echo 'Deactivating virtual environment'
                bat '.\\venv\\Scripts\\deactivate'
            }
        }
    }
}
