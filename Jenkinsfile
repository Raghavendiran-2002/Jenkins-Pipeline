pipeline {
  agent any
  stages {
    stage('Build Container') {
      steps {
        sh 'cd /Users/raghavendiran/Desktop/Jenkins-Pipeline'
        sh 'git pull origin main'
        sh 'echo honda4104 | sudo -S echo "SuperUser"'
        sh 'docker system prune -a -f && docker-compose up -d'
      }
    }
  }
}
