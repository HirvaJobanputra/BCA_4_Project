document.getElementById("log-in-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    isValid=true;
    const username = document.getElementById("userName").value.trim();
    const password = document.getElementById("password").value.trim();

    // Clear previous error messages
    document.getElementById("usernameError").innerHTML = "";
    document.getElementById("passwordError").innerHTML = "";

    if (username === "") {
        document.getElementById("usernameError").innerHTML = "**Please enter your username.";
    }

    if (password === "") {
        document.getElementById("passwordError").innerHTML = "**Please enter your password.";
    }
    const usernameRegex=/^[a-zA-Z0-9_-]{3,30}$/;

    const passwordRegex=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]).{8,}$/;
    if (username !== "" && !usernameRegex.test(username)) {
        alert("Please enter a valid username!!!");
        isValid = false;
    }

    if (password !== "" && !passwordRegex.test(password)) {
        alert("Enter a valid password!!!");
        isValid = false;
    }

    if (isValid) {
        window.location.href = "home.html";
    }   
});