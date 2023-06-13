node {
  stage('Github') {
    checkout scm
  }
  // stage('SonarQube Analysis') {
  //   def scannerHome = tool 'SonarScanner';
  //   withSonarQubeEnv() {
  //     sh "${scannerHome}/bin/sonar-scanner"
  //   }
  // }
  stage('API Testing'){
    agent {
      docker { dockerfile true }
    }
    sh '''chmod +x tests.sh
          sh tests.sh
          cat result.txt'''
  }
  // stage('Clear'){
  //   cleanWs()
  // }
}