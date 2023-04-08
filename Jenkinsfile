pipeline {
  agent any
  stages {
    stage('Build Container') {
      steps {
        sh "echo honda4104 | sudo -S echo 'Approved'"
        sh 'npm i && node index.js'

      }
    }
  }
}
