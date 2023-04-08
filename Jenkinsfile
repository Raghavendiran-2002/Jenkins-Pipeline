pipeline {
  agent any
  stages {
    stage('Build Container') {
      steps {
        sh "git clone https://github.com/Raghavendiran-2002/Jenkins-Pipeline.git && cd Jenkins-Pipeline/"
        sh "echo honda4104 | sudo -S"
        sh "sudo docker-compose up -d"
        sh 'echo "Completed"'
      }
    }
  }
}
