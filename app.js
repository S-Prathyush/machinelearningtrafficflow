const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const port = 3000;

// Connect to SQLite database
const db = new sqlite3.Database('./database.db');

// Create user table if not exists with two columns: s_no and user_feedback
db.run(`CREATE TABLE IF NOT EXISTS users (
    s_no INTEGER PRIMARY KEY AUTOINCREMENT,
    user_feedback TEXT
)`);

// Middleware to parse JSON bodies
app.use(express.json());

// Serve static files (HTML, CSS, etc.)
const publicPath = path.join(__dirname);
app.use(express.static(publicPath));

// Route for serving the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(publicPath, 'index.html'));
});

// Route for handling form submission
app.post('/submit-feedback', (req, res) => {
    const userFeedback = req.body.feedback;

    // Insert user feedback into database
    db.run('INSERT INTO users (user_feedback) VALUES (?)', [userFeedback], function(err) {
        if (err) {
            return res.status(500).json({ message: 'Error saving feedback' });
        }
        console.log(`A row has been inserted with rowid ${this.lastID}`);
        res.status(200).json({ message: 'Feedback submitted successfully' });
    });
});

// Route for retrieving data from the database and displaying it in a table
app.get('/feedbacks', (req, res) => {
    db.all('SELECT * FROM users', (err, rows) => {
        if (err) {
            return res.status(500).json({ message: 'Error retrieving feedbacks' });
        }
        res.json(rows);
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
