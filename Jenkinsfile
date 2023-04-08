pipeline {
  agent any
  stages {
    stage('Build Container') {
      steps {
        sh 'cd /Users/raghavendiran/Desktop/Jenkins-Pipeline'
        sh 'git pull origin main'
        sh 'sudo docker system prune -a -f && sudo docker-compose up -d'
      }
    }
  }
}
