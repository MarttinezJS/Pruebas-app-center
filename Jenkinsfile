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
      docker {     
        image 'python:3.9-slim'
        args '-u root --privileged'
      }
    }
    sh 'apt-get update'
    sh 'apt-get install python-pip'
    sh 'pip install pytest'
    sh 'pytest tests.py'
  }
  //   sh '''chmod +x tests.sh
  //         sh tests.sh
  //         cat result.txt'''
  // }
  // stage('Clear'){
  //   cleanWs()
  // }
}