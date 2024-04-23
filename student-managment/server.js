const express = require('express');
const mysql2 = require('mysql2');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

const db = mysql2.createConnection({
    host: 'localhost',
    user: 'root',
    password: '1251Rama1251@rshafii106', // Change to your mysql2 password
    database: 'student_managment_system'
});

db.connect((err) => {
    if (err) throw err;
    console.log('mysql2 connected');
});

// Serve static files from the default directory
app.use(express.static(__dirname));

// Set up middleware to parse incoming JSON data
app.use(express.json());
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/addStudent', (req, res) => {
    // Extract student data from the request body
    const { name, age, grade } = req.body;

    // SQL query to insert a new student record into the database
    const sql = 'INSERT INTO students (name, age, grade) VALUES (?, ?, ?)';
    
    // Execute the SQL query with the student data
    db.query(sql, [name, age, grade], (err, result) => {
        if (err) {
            console.error('Error adding student:', err);
            res.status(500).send('Error adding student to the database');
            return;
        }
        console.log('Student added successfully');
        res.status(200).send('Student added successfully');
    });
});

app.get('/students', (req, res) => {
    const sql = 'SELECT * FROM students';
    db.query(sql, (err, result) => {
        if (err) throw err;
        res.json(result);
    });
});

app.delete('/deleteStudent/:id', (req, res) => {
    const id = req.params.id;
    const sql = 'DELETE FROM students WHERE id = ?';
    db.query(sql, id, (err, result) => {
        if (err) throw err;
        res.send('Student deleted successfully');
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});