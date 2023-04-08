pipeline {
  agent any
  stages {
    stage('Build Container') {
      steps {
        sh 'cd /Users/raghavendiran/Desktop/Jenkins-Pipeline'
        sh 'git pull origin main'
        sh 'echo honda4104 | sudo -S echo "SuperUser"'
        sh 'sudo docker system prune -a -f && sudo docker-compose up -d'
      }
    }
  }
}
