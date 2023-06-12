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
    def testImage = docker.build("test-image", "./Dockerfile.test") 
    testImage.inside {
        sh '''rm -rf reports; mkdir reports
            pytest app/test/test.py -s -v'''
    }
    // sh '''IMAGE_NAME="test-image"
    //   CONTAINER_NAME="test-container"
    //   echo "Check current working directory"
    //   pwd
    //   echo "Build docker image and run container"
    //   docker build -t $IMAGE_NAME -f Dockerfile.test .
    //   docker run -d --name $CONTAINER_NAME --network pruebas-app-center_tdd_tests --env DB_NAME=tests --env DB_USER=root --env DB_PASSWORD=root --env DB_HOST=mongo $IMAGE_NAME
    //   echo "Copy result into Jenkins container"
    //   rm -rf reports; mkdir reports
    //   echo "Cleanup"
    //   docker stop $CONTAINER_NAME
    //   docker cp $CONTAINER_NAME:/code/result.txt reports/
    //   docker rm $CONTAINER_NAME
    //   docker rmi $IMAGE_NAME'''
  }
  // stage('Clear'){
  //   cleanWs()
  // }
}