pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:/Users/karan/AppData/Local/Programs/Python/Python312;C:/Users/karan/AppData/Local/Programs/Python/Python312/Scripts'
        SONAR_SCANNER_PATH = 'C:/Users/karan/Downloads/sonar-scanner-cli-6.2.1.4610-windows-x64/sonar-scanner-6.2.1.4610-windows-x64/bin'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                python --version
                pip --version
                pip install -r requirements.txt
                '''
            }
        }
        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonar-token') // Corrected to use `credentials`
            }
            steps {
                bat '''
                set PATH=%SONAR_SCANNER_PATH%;%PATH%
                where sonar-scanner || echo "SonarQube scanner not found. Please ensure it is installed and correctly configured."
                sonar-scanner -Dsonar.projectKey=test ^
                               -Dsonar.sources=. ^
                               -Dsonar.host.url=http://localhost:9000 ^
                               -Dsonar.login=%SONAR_TOKEN%
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
