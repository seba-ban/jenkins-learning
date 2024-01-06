pipeline {
    agent { docker { image 'python:3.11' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m venv .venv'
                sh '.venv/bin/pip install poetry poethepoet'
                sh 'mkdir -p .cache'
                sh 'POETRY_CACHE_DIR=$(pwd)/.cache POETRY_VIRTUALENVS_CREATE=True .venv/bin/poetry install --no-cache'
                sh '.venv/bin/poe test'
            }
        }
    }
}