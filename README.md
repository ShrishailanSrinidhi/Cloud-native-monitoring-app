# Cloud-native-monitoring-app
=======
# Steps:
1) Create a python flask app.
2) Create a Docker file.
3) Build DockerImage.
4) Test Docker container locally.
5) Create ECR repository using Python Boto3 and pushing Docker Image to ECR.
6) Create EKS cluster and Nodegroups.
7) Create Kubernetes Deployments and Services using Python!

# Create a python flask app
## Clone the code from the repository
~~~
git clone git@github.com:ShrishailanSrinidhi/Cloud-native-monitoring-app.git
~~~

## Install Dependencies
The application uses the psutil and Flask, Plotly, boto3 libraries. Install them using pip:
~~~
pip3 install -r requirements.txt
~~~

## Run the Application
~~~
python3 app.py
~~~

This will start the Flask server on localhost:5000. Navigate to http://localhost:5000/ on your browser to access the application.

# Dockerize the Python App
## Create DockerFile
Create a Dockerfile in the root directory of the project with the following contents:
~~~
# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app when the container is run
CMD ["flask", "run"]
~~~

## Run the Docker Container
~~~
docker run -p 5000:5000 <image_name>
~~~

This will start the Flask server in a Docker container on localhost:5000. Navigate to http://localhost:5000/ on your browser to access the application.
>>>>>>> ba1be1f (Update README)
