# Full-Stack Application with Node.js/Express Frontend and Flask Backend

This is a full-stack application with a Node.js/Express frontend and a Flask backend, containerized using Docker.

## Project Structure

```
.
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── app.js
│   ├── package.json
│   └── views/
│       └── index.ejs
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Build and run the application using Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000

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
