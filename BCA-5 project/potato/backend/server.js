const express = require("express");
// const cors = require("cors");
const app = express();
const db = require('./db');
const port = 5000;

// app.use(cors());
app.use(express.json());
app.use("/users", require("./routes/users"));
app.listen(port, () => console.log(`🚀 Server running on http://localhost:${port}`));
app.use("/categories", require("./routes/category"));
app.listen(port, () => console.log(`🚀 Server running on http://localhost:${port}`));
app.use("/menu_items", require("./routes/menu_items"));
app.listen(port, () => console.log(`🚀 Server running on http://localhost:${port}`));
