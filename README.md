# Task-Application-Docker-Kubernetes
Created Task Manager using Docker and Kubernetes
<br>
This application uses Flask and MongoDB. Its main purpose is to allow users to add, complete, and delete tasks. The application is containerized using Docker and can be deployed using Kubernetes.
<be>
Uses Github Actions Workflow to automate the process and verifying it
## Prerequisites
- Docker and Docker Compose installed
- Kubernetes cluster
- Python 3.9 installed
- `kubectl` CLI installed

## Setup
1. Clone the Repository (This can be done by clicking on the code, copy the link, and use `git clone <URL>`. )
 ```
git clone <url>
``` 
2. Setup the environment variables.

## Docker Setup
Start Docker desktop and keep it running in the background.
```
docker-compose up --build
```
```
http://localhost:5000
```

## Kubernetes Setup
Setup the Secrets and ConfigMap.
```
kubectl apply -f kubernetes/
```
Then run the following command to access the application
```
kubectl get services
```
or
```
minikube service flask-service --url
```

