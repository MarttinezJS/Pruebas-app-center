pipeline{
    agent{
        label "python"
    }
    stages{
        stage('Github'){
            steps{
              checkout scm
              sh ('python3.10 --version')
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
      // stage('SonarQube Analysis') {
      //   def scannerHome = tool 'SonarScanner';
      //   withSonarQubeEnv() {
      //     sh "${scannerHome}/bin/sonar-scanner"
      //   }
      // }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
