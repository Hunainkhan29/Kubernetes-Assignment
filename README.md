# 🚀 Fullstack Application with Kubernetes

A **fullstack application** featuring a **Flask backend** and **Express frontend**, containerized with **Docker** and orchestrated using **Kubernetes**.

---

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop) — installed and running  
- [kubectl](https://kubernetes.io/docs/tasks/tools/) — Kubernetes command-line tool  
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) — for local Kubernetes cluster  
- [Git](https://git-scm.com/downloads) — for cloning the repository  

---

## 🏗️ Project Structure


├── backend/ # Flask backend
│ ├── Dockerfile # Backend Dockerfile
│ ├── app.py # Flask application
│ └── requirements.txt # Python dependencies
│
├── frontend/ # Express frontend
│ ├── Dockerfile # Frontend Dockerfile
│ ├── app.js # Express application
│ ├── package.json # Node.js dependencies
│ └── views/
│ └── index.ejs # Frontend template
│
├── k8s/ # Kubernetes manifests
│ ├── backend-deployment.yaml
│ ├── backend-service.yaml
│ ├── frontend-deployment.yaml
│ └── frontend-service.yaml
│
├── docker-compose.yml # Docker Compose configuration
└── README.md # This file



---

## 🚀 Quick Start with Docker Compose

1. **Clone the repository**
   ```bash
   git clone <https://github.com/Hunainkhan29/Kubernetes-Assignment>
   cd Docker

2. Start the application

docker-compose up -d


Access the application

Frontend: http://localhost:3000

Backend API: http://localhost:5000


☸️ Kubernetes Deployment
1. Start Minikube
   minikube start --driver=docker
minikube status

2. Build and Push Docker Images
docker-compose build

docker tag fullstack-backend yourusername/fullstack-backend:latest
docker tag fullstack-frontend yourusername/fullstack-frontend:latest

docker push yourusername/fullstack-backend:latest
docker push yourusername/fullstack-frontend:latest

3. Deploy to Kubernetes
cd k8s
kubectl apply -f .

4. Access the Application
minikube service frontend-service
# OR
kubectl port-forward service/frontend-service 3000:3000

🛠️ Useful Commands
Kubernetes
# View all resources
kubectl get all

# View pod logs
kubectl logs <pod-name>

# Scale deployments
kubectl scale deployment backend-deployment --replicas=3
kubectl scale deployment frontend-deployment --replicas=3

Docker
# Build images
docker-compose build

# Start containers
docker-compose up -d

# View logs
docker-compose logs -f

🧹 Cleanup
Docker Compose
docker-compose down

Kubernetes
# Delete all resources
kubectl delete -f .

# Stop Minikube
minikube stop

# Delete Minikube cluster
minikube delete

📝 Troubleshooting
Common Issues
Problem	Solution
Port already in use	Stop any service using ports 3000 or 5000.
Image pull errors	Ensure your images are built and pushed to Docker Hub.
Pods not starting	View logs using: kubectl logs <pod-name>.
📚 Documentation

Kubernetes Documentation

Minikube Documentation

Docker Documentation

