# AWS Deployment Guide

This guide provides instructions for deploying the application on AWS using different architectures.

## Prerequisites
- AWS Account
- AWS CLI configured with appropriate permissions
- Docker installed locally
- Git installed

---

## 1. Single EC2 Instance Deployment

### Steps:
1. **Launch an EC2 Instance**
   - AMI: Amazon Linux 2
   - Instance Type: t2.micro (Free Tier eligible)
   - Security Group: Open ports 22 (SSH), 80 (HTTP), 3000 (Frontend), 5000 (Backend)
   - IAM Role: EC2 Role with ECR access

2. **Connect to EC2 Instance**
   ```bash
   ssh -i your-key.pem ec2-user@your-instance-public-dns
   ```

3. **Install Dependencies**
   ```bash
   sudo yum update -y
   sudo amazon-linux-extras install docker -y
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

4. **Deploy Application**
   ```bash
   git clone https://github.com/Hunainkhan29/Docker-Assignment.git
   cd Docker-Assignment
   docker-compose up -d
   ```

5. **Access Application**
   - Frontend: http://your-instance-public-dns:3000
   - Backend: http://your-instance-public-dns:5000

---

## 2. Separate EC2 Instances

### Frontend Instance
1. **Launch EC2 Instance**
   - Same as above, but only open ports 80 and 3000

2. **Deploy Frontend**
   ```bash
   # Install Docker and Docker Compose (same as above)
   git clone https://github.com/Hunainkhan29/Docker-Assignment.git
   cd Docker-Assignment/frontend
   docker build -t frontend .
   docker run -d -p 3000:3000 frontend
   ```

### Backend Instance
1. **Launch EC2 Instance**
   - Same as above, but only open ports 22 and 5000

2. **Deploy Backend**
   ```bash
   # Install Docker and Docker Compose (same as above)
   git clone https://github.com/Hunainkhan29/Docker-Assignment.git
   cd Docker-Assignment/backend
   docker build -t backend .
   docker run -d -p 5000:5000 backend
   ```

3. **Update Frontend Configuration**
   In the frontend's `app.js`, update the backend URL to point to the backend instance's public DNS.

---

## 3. ECS with ECR and VPC

### 1. Push Images to ECR

```bash
# Login to ECR
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com

# Create ECR Repositories
aws ecr create-repository --repository-name fullstack-frontend
aws ecr create-repository --repository-name fullstack-backend

# Tag and push images
docker tag hunainkhan29/fullstack-frontend:latest your-account-id.dkr.ecr.your-region.amazonaws.com/fullstack-frontend:latest
docker push your-account-id.dkr.ecr.your-region.amazonaws.com/fullstack-frontend:latest

docker tag hunainkhan29/fullstack-backend:latest your-account-id.dkr.ecr.your-region.amazonaws.com/fullstack-backend:latest
docker push your-account-id.dkr.ecr.your-region.amazonaws.com/fullstack-backend:latest
```

### 2. Create ECS Cluster
1. Go to ECS Console
2. Create a new cluster
3. Select "Networking only" and click "Next"
4. Configure VPC and subnets
5. Create an Application Load Balancer

### 3. Create Task Definitions
Create two task definitions (one for frontend, one for backend) with container definitions pointing to your ECR images.

### 4. Create Services
Create services for both frontend and backend tasks, attaching them to your load balancer.

### 5. Access Application
Use the DNS name of your load balancer to access the application.

---

## Cost Optimization
- Use t2.micro instances for development (Free Tier eligible)
- Set up billing alerts in AWS
- Stop instances when not in use
- Consider using AWS Fargate for serverless containers

## Security Best Practices
- Use security groups to restrict access
- Store sensitive data in AWS Secrets Manager
- Enable VPC Flow Logs
- Use IAM roles instead of access keys when possible

## Monitoring
- Set up CloudWatch Alarms
- Enable Container Insights for ECS
- Monitor costs in AWS Cost Explorer

## Cleanup
Remember to delete all resources when not in use to avoid unnecessary charges:
- Terminate EC2 instances
- Delete ECR repositories
- Delete ECS clusters
- Remove unused security groups and load balancers
