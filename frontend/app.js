const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Set EJS as view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Routes
app.get('/', (req, res) => {
    res.render('index', { result: null, error: null });
});

app.post('/submit', async (req, res) => {
    try {
        // Support both Docker Compose (backend) and Kubernetes (backend-service)
        const backendUrl = process.env.BACKEND_URL || 'http://backend:5000';
        const response = await axios.post(`${backendUrl}/process`, req.body);
        res.render('index', { result: response.data, error: null });
    } catch (error) {
        console.error('Error:', error.message);
        res.render('index', { result: null, error: 'Error processing your request' });
    }
});

app.listen(PORT, () => {
    console.log(`Frontend server running on http://localhost:${PORT}`);
});
