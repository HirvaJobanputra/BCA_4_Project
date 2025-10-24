const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const users = JSON.parse(localStorage.getItem('users')) || [];

    const user = users.find(u => u.username === username && u.password === password);

    if (user) {
        // Login successful
        alert('Login successful!');
        // Redirect to quiz page or user dashboard
        window.location.href = 'home.html'; // Or whatever your quiz page is named.
    } else {
        // Login failed
        alert('Invalid username or password.'); // Changed error message
    }
});