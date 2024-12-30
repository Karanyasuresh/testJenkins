pipeline{
  agent any
  environment{
    PYTHON_PATH='C:/Users/karan/AppData/Local/Programs/Python/Python312;C:/Users/karan/AppData/Local/Programs/Python/Python312/Scripts'
  }
  stages{
    stage('checkout'){
      steps{
        checkout scm
      }
    }
  stage('build'){
    steps{
      bat '''
      set PATH=%PYTHON_PATH%;%PATH%
      pip install -r requirement.txt
      '''
    }
  }
  stage('sonarqube-Analysis'){
    environment{
      SONAR_TOKEN=cfredentials('sonar-token')
    }
   steps {
                // Ensure that sonar-scanner is in the PATH
                bat '''
                set PATH=%SONAR_SCANNER_PATH%;%PATH%
                where sonar-scanner || echo "SonarQube scanner not found. Please install it."
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=test ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.token=%SONAR_TOKEN%
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
  
