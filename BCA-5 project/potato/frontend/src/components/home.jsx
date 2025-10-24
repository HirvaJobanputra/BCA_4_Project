import React from "react";
import "../home.css"; // External CSS file

function Home() {
    const categories = [
        { name: "South Indian", image: "/images/dosa.jpg" },
        { name: "North Indian", image: "/images/north.jpeg" },
        { name: "Chinese", image: "/images/noodles.jpeg" },
        { name: "Italian", image: "/images/pasta.jpeg" },
        { name: "Mexican", image: "/images/salsa.jpeg" },
        { name: "Desserts", image: "/images/dessert.jpeg" },
        { name: "Beverages", image: "/images/coffee.jpeg" },
        { name: "Bakery", image: "/images/cake.jpeg" },
        { name: "Rice", image: "/images/rice.jpeg" },
        { name: "Salads", image: "/images/salad.jpeg" },
    ];

    const handleCategoryClick = (categoryName) => {
        console.log(`Open ${categoryName} menu here`);
        // Placeholder for navigation or popup logic
    };

    const handleGenerateBill = () => {
        console.log("Generate bill functionality here");
        // Placeholder for bill generation logic
    };

    return (
        <div className="container">
            <header>
                <h1>Welcome to Potato 🥔</h1>
            </header>

            <main>
                <div className="card-grid">
                    {categories.map((cat, index) => (
                        <div
                            key={index}
                            className="card"
                            onClick={() => handleCategoryClick(cat.name)}
                        >
                            <img src={cat.image} alt={cat.name} />
                            <h3>{cat.name}</h3>
                        </div>
                    ))}
                </div>
            </main>

            <footer>
                <button onClick={handleGenerateBill}>Generate Bill</button>
            </footer>
        </div>
    );
}

export default Home;
