const express = require("express");
const router = express.Router();
const db = require("../db");

// --- Get all users ---
router.get('/', (req, res) => {
    const sql = "SELECT * FROM users";
    db.query(sql, (err, data) => {
        if (err) return res.json(err);
        return res.json(data);
    });
});

// --- Add user ---
router.post('/', (req, res) => {
    const sql = "INSERT INTO users (email, password) VALUES (?, ?)";
    const values = [req.body.email, req.body.password];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json("✅ User created successfully");
    });
});

// --- Update user ---
router.put('/:id', (req, res) => {
    const sql = "UPDATE users SET email = ?, password = ? WHERE userID = ?";
    const values = [req.body.email, req.body.password, req.params.id];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json("✅ User updated successfully");
    });
});

// --- Delete user ---
router.delete('/:id', (req, res) => {
    const sql = "DELETE FROM users WHERE userID = ?";
    const values = [req.params.id];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json("✅ User deleted successfully");
    });
});

module.exports = router;
