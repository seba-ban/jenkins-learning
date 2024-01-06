pipeline {
    agent { docker { image 'python:3.11' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m venv .venv'
                sh '.venv/bin/pip install poetry poethepoet'
                sh 'mkdir .cache'
                sh '.venv/bin/poetry config set cache-dir $(pwd)/.cache'
                sh '.venv/bin/poetry install --no-cache'
                sh '.venv/bin/poe test'
            }
        }
    }
}