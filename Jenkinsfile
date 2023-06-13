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
      docker { image 'python:slim'}
    }
    sh '''apt-get update
          apt-get install -y python-pip
          pip --version'''
    // sh '''python3 -m pip install pytest
    //   chmod +x tests.sh
    //   sh tests.sh
    //   cat result.txt'''
  }
  // stage('Clear'){
  //   cleanWs()
  // }
}