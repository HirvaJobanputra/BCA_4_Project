document.addEventListener('DOMContentLoaded',function(){
    
    const loginForm = document.getElementById('login-form');

    loginForm.addEventListener('submit', function(event){
        event.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Retrive stored user details from localstorage
        const storedUser = localStorage.getItem(username);
        if (storedUser === null){
            alert("User not found. Please sign up.");
            return;
        }
        else{
            const user = JSON.parse(storedUser);
            if (user.password !== btoa(password)){
                alert("Incorrect password. Please try again.");
                return;
            }
            else{
                alert("Login successful!");
                window.location.href = 'home.html';
                loginForm.reset();
            }
        }
    });

})