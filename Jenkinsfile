pipeline {
    agent { docker { image 'python:3.12' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install poetry poethepoet'
                sh 'poetry install'
                sh 'poe test'
            }
        }
    }
}