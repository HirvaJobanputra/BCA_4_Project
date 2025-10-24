const express = require("express");
const router = express.Router();
const db = require("../db");

// --- Get all categories ---
router.get('/', (req, res) => {
    const sql = "SELECT * FROM categories";
    db.query(sql, (err, data) => {
        if (err) return res.json(err);
        return res.json(data);
    });
});

// --- Add category ---
router.post('/', (req, res) => {
    const sql = "INSERT INTO categories (name) VALUE (?)";
    const values = [req.body.name];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json(" Category created successfully");
    });
});

// --- Update category ---
router.put('/:id', (req, res) => {
    const sql = "UPDATE categories SET name = ? WHERE categoryID = ?";
    const values = [req.body.name, req.params.id];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json(" Category updated successfully");
    });
});

// --- Delete category ---
router.delete('/:id', (req, res) => {
    const sql = "DELETE FROM categories WHERE categoryID = ?";
    const values = [req.params.id];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json(" Category deleted successfully");
    });
});

module.exports = router;
