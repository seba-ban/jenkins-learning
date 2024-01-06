pipeline {
    agent { docker { image 'python:3.11' } }
    stages {
        stage('build') {
            steps {
                sh 'sleep 3600'
                sh 'pip install poetry poethepoet'
                sh 'poetry install'
                sh 'poe test'
            }
        }
    }
}