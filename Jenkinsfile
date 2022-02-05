pipeline{
  agent any 
  stages {
    stage('Build') {
      steps {
        sh ('curl --version')
      }
    }
    stage('Test') {
      steps {
        echo "Testing stages!!!!"
      }
    }
  
    stage('Deploy') {
      steps {
        echo "Deploying stages"
      }
    }
  }
}
