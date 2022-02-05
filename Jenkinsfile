pipeline{
  agent any 
  stages {
    stage('Build') {
      steps {
        def response = httpRequest 'http://google.com'
            println("Status": "+response.code")
            println("Content": "+response.content")
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
