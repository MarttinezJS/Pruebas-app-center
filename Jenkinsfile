node {
  stage('Github') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Testing'){
    steps{
      def scriptTest = "${WORKSPACE}/tests.sh"
      sh "chmod +x ${scriptTest} && sh ${scriptTest}"
    }
  }
  stage('Clear'){
    cleanWs()
  }
}