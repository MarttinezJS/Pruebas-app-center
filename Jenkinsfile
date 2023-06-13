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
    step {
      sh '''IMAGE_NAME="test-image"
          CONTAINER_NAME="test-container"
          echo "Check current working directory"
          pwd
          echo "Build docker image and run container"
          docker build -t $IMAGE_NAME -f Dockerfile.test .
          docker run -d --name $CONTAINER_NAME -e DB_HOST=mongodb+srv://jhonatan:D8JNwKf1bsO2kJtL@estudio.evopu.mongodb.net/tests $IMAGE_NAME
          echo "Copy result into Jenkins container"
          rm -rf reports; mkdir reports
          echo "Cleanup"
          docker stop $CONTAINER_NAME
          docker cp $CONTAINER_NAME:/code/result.txt reports/
          docker rm $CONTAINER_NAME
          docker rmi $IMAGE_NAME'''
    }
    post{
      always{
        sh '''IMAGE_NAME="test-image"
            CONTAINER_NAME="test-container"
            docker stop $CONTAINER_NAME
            docker rm $CONTAINER_NAME
            docker rmi $IMAGE_NAME'''
      }
    }
  //   agent {
  //     docker {     
  //       image 'python:3.9-slim'
  //       args '-u root --privileged'
  //     }
  //   }
  //   sh 'apt-get install python-pip'
  //   sh 'pip install pytest'
  //   sh 'pytest tests.py'
  // }
  }
  // stage('Clear'){
  //   cleanWs()
  // }
}