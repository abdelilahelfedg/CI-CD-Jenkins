pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github-token')
        VENV_DIR = ".venv"
        PYTHON = "${WORKSPACE}\\.venv\\Scripts\\python.exe"
        PIP = "${WORKSPACE}\\.venv\\Scripts\\pip.exe"
        GUNICORN = "${WORKSPACE}\\.venv\\Scripts\\gunicorn.exe"
        HOST = "0.0.0.0"
        PORT = "5000"
        APP_MODULE = "app:app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/abdelilahelfedg/CI-CD-Jenkins.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                "C:\\Users\\HP 830G8\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv ${VENV_DIR}
                ${PYTHON} -m pip install --upgrade pip
                ${PIP} install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            when {
                not {
                    changeset "README.md"
                }
            }
            parallel {
                stage('Test File 1') {
                    steps {
                        bat """
                        ${PYTHON} -m pytest test_app.py -v
                        """
                    }
                }
                
            }
        }

        stage('Deploy (Local with Gunicorn)') {
            steps {
                echo 'Starting Flask app locally using Gunicorn...'
                bat """
                start /B ${GUNICORN} --bind ${HOST}:${PORT} ${APP_MODULE} > gunicorn.log 2>&1
                echo Gunicorn started on http://${HOST}:${PORT}
                """
            }
        }
    }

    post {
        success {
            emailext(
                to: "EMAIL_TO_PLACEHOLDER",
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build succeeded: ${env.BUILD_URL}"
            )
        }

        failure {
            emailext(
                to: "EMAIL_TO_PLACEHOLDER",
                subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build failed: ${env.BUILD_URL}"
            )
        }
    }
}
