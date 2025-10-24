const mysql = require('mysql2');
const express = require('express');
const app = express();
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'potato',
});

db.connect((err) => {
    if (err) {
        console.error("Connection failed!!", err.message);
        return;
    }
    console.log("Successfully Connected to MySQL");
});

module.exports = db;

// app.use('/routes/api/categories', require('./routes/api/categories'));
// app.use('/routes/api/menu_items', require('./routes/api/menu_items'));
// app.use('/routes/api/users', require('./routes/api/users'));