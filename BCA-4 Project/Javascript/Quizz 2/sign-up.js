document.addEventListener('DOMContentLoaded', function() { // Wait for the DOM to load

    const signupForm = document.getElementById('signup-form');

    signupForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password').value;

        let isValid = true; // Assume valid until proven otherwise

        // Username validation (example: alphanumeric, 3-20 characters)
        const usernameRegex =/^(?![0-9]+$)[a-zA-Z][a-zA-Z0-9_]{2,19}$/;
        if (!usernameRegex.test(username)) {
            alert("Username must be alphanumeric and between 3 and 20 characters.");
            isValid = false;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Please enter a valid email address.");
            isValid = false;
        }

        // Password validation (example: at least 8 characters, one uppercase, one lowercase, one number)
        const passwordRegex =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-])[a-zA-Z\d!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]{8,}$/;
        if (!passwordRegex.test(password)) {
            alert("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.");
            isValid = false;
        }

        // Confirm password validation
        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            isValid = false;
        }

        if (isValid) {
            // Store user details in localStorage
            const user = {
                username: username,
                email: email,
               // password: password // NEVER STORE PASSWORD IN PLAIN TEXT
               password: btoa(password) // store a BASE64 encoded password.  Still NOT SECURE but better than plain text.  NEVER use in production.
            };

            localStorage.setItem(username, JSON.stringify(user));  //Key is the username.
            alert("Sign up successful!");
            window.location.href = 'home.html'; 
            
            signupForm.reset();

        }
    });
});