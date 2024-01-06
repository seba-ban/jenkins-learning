pipeline {
    agent { docker { image 'python:3.11' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m venv .venv'
                sh '.venv/bin/pip install poetry poethepoet'
                sh '.venv/bin/poetry install'
                sh '.venv/bin/poe test'
            }
        }
    }
}