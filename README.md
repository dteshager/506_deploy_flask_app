# 506_deploy_flask_app
This is a basic Flask application containerized wiht Docker. The app demonstrates how to run a simple python web server using Flask inside a Docker container. It uses python 3.11 and Flask 3.1.0.
It's a lightweight Flask web app Contanerized with Docker.

## Requirements

-Docker installed on your system. <br>
-Python dependencies are managed inside the docker container.

## How to run 
### 1. Build the Docker Image

Open the terminal in the project directory (where the Dockerfile is located) and run: docker build -t flask_app:0.0.1.RELEASE . 

### 2. Run the Docker container

docker run -p 5000:5000 flask_app:0.0.1.RELEASE
after you run the above command you can open your browser and go to: http://localhost:5000

