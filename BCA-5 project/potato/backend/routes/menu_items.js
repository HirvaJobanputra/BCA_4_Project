const express = require("express");
const router = express.Router();
const db = require("../db");

// --- Get all menu items ---
router.get('/', (req, res) => {
    const sql = "SELECT * FROM menu_items";
    db.query(sql, (err, data) => {
        if (err) return res.json(err);
        return res.json(data);
    });
});

// --- Add menu item ---
router.post('/', (req, res) => {
    const sql = "INSERT INTO menu_items (name, price, categoryID) VALUES (?, ?, ?)";
    const values = [req.body.name, req.body.price, req.body.categoryID];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json("Menu item created successfully");
    });
});

// --- Update menu item ---
router.put('/:id', (req, res) => {
    const sql = "UPDATE menu_items SET name = ?, price = ?, categoryID = ? WHERE menu_id = ?";
    const values = [req.body.name, req.body.price, req.body.categoryID, req.params.id];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json("Menu item updated successfully");
    });
});

// --- Delete menu item ---
router.delete('/:id', (req, res) => {
    const sql = "DELETE FROM menu_items WHERE menu_id = ?";
    const values = [req.params.id];
    db.query(sql, values, (err, data) => {
        if (err) return res.json(err);
        return res.json("Menu item deleted successfully");
    });
});

module.exports = router;