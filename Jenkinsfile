pipeline {
    agent { docker { image 'python:3.11' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m venv .venv'
                sh '. .venv/bin/activate'
                sh 'pip install poetry poethepoet'
                sh 'poetry install'
                sh 'poe test'
            }
        }
    }
}