# Full-Stack Application with Node.js/Express Frontend and Flask Backend

This is a full-stack application with a Node.js/Express frontend and a Flask backend, containerized using Docker.

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hunainkhan29/Docker-Assignment.git
   cd Docker-Assignment
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

## 📦 Docker Images
- **Frontend**: [hunainkhan29/fullstack-frontend](https://hub.docker.com/r/hunainkhan29/fullstack-frontend)
- **Backend**: [hunainkhan29/fullstack-backend](https://hub.docker.com/r/hunainkhan29/fullstack-backend)

## 🏗️ Project Structure

```
.
├── backend/               # Flask backend
│   ├── Dockerfile        # Backend Dockerfile
│   ├── app.py            # Flask application
│   └── requirements.txt  # Python dependencies
├── frontend/             # Express frontend
│   ├── Dockerfile        # Frontend Dockerfile
│   ├── app.js            # Express application
│   ├── package.json      # Node.js dependencies
│   └── views/
│       └── index.ejs     # Frontend template
├── docker-compose.yml    # Docker Compose configuration
└── README.md             # This file
```

## 🛠️ Development

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. **Development mode**
   ```bash
   # Start both frontend and backend
   docker-compose up
   
   # Or run in detached mode
   docker-compose up -d
   ```

2. **View logs**
   ```bash
   # View all logs
   docker-compose logs
   
   # View logs for a specific service
   docker-compose logs frontend
   docker-compose logs backend
   ```

3. **Stop the application**
docker-compose down
   ```

## 🌐 API Endpoints

- `GET /` - Welcome message
- `POST /process` - Process form data

## 📝 Notes
- The frontend runs on port 3000
- The backend API runs on port 5000
- The services communicate via Docker's internal network

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Features

- **Frontend**: Built with Node.js and Express, serving an EJS template
- **Backend**: RESTful API built with Flask
- **Docker**: Containerized application with Docker and Docker Compose

## API Endpoints

- `GET /` - Welcome message
- `POST /process` - Process form data

## Development

### Frontend Development

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend Development

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask development server:
   ```bash
   flask run
   ```

## Deployment

1. Build and push the Docker images to Docker Hub:
   ```bash
   # Build the images
   docker-compose build
   
   # Tag the images
   docker tag <frontend-image-id> yourusername/frontend:latest
   docker tag <backend-image-id> yourusername/backend:latest
   
   # Push to Docker Hub
   docker push yourusername/frontend:latest
   docker push yourusername/backend:latest
   ```

2. Update the `docker-compose.yml` file with your Docker Hub image names.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
