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
    withPythonEnv('python3'){
      sh 'pip install pytest'
      sh 'pytest tests.py'
    }
  }
  //   agent {
  //     docker { dockerfile true }
  //   }
  //   sh '''chmod +x tests.sh
  //         sh tests.sh
  //         cat result.txt'''
  // }
  // stage('Clear'){
  //   cleanWs()
  // }
}