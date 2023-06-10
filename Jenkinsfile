node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}


// pipeline {
//     agent any
//     stages {
//         stage('Github') {
//             steps {
//                 git 'https://github.com/MarttinezJS/Pruebas-app-center.git'
//             }
//         }
//         stage('SonarQube'){
//             steps{
                
//             }
//         }
//         stage('API Testing'){
//             steps{
//                 sh 'chmod +x /var/jenkins_home/workspace/appcenter-api-tests/run.sh'
//                 sh '/var/jenkins_home/workspace/appcenter-api-tests/run.sh'
//             }
//         }
//     }
// }