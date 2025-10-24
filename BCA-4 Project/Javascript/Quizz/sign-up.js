const signupForm=document.getElementById('signup-form');
signupForm.addEventListener('submit',(e) => {
    e.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;
            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }
            let users = JSON.parse(localStorage.getItem('users')) ||[]
            users.push({ username, email, password });
            localStorage.setItem('users', JSON.stringify(users));

            // Redirect to login page or display success message
            alert('Signup successful!.');
            window.location.href = 'home.html'; 
        });
        function check(){

            const username=document.getElementById("username").value;
            const email =   document.getElementById("email").value;
            const password =   document.getElementById("password").value;
            const confirm_password =   document.getElementById("confirm-password").value;
        
            const usernameRegex=/^[a-zA-Z0-9_-]{3,16}$/;
            const emailRegex=/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            const passwordRegex=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        
        
            let isvalid = true;
            if(usernameRegex.test(username)){
                username.style.border  = "2px solid green";
            }
            else{
                alert("Invalid Username Format:");
                isvalid=false;
            }
            if(emailRegex.test(email)){
                email.style.border="2px solid green";
            }
            else{
                alert("Invalid Email");
                isvalid=false;
            }
            if(passwordRegex.test(password)){
                password.style.border  = "2px solid green";
        
            }
            else{
                alert("Invalid password format | Password must contain at least 8 characters, including uppercase, lowercase letters, numbers and special characters");
                isvalid=false;
            }
            if(password.value===confirm_password.value){
                confirm_password.style.border  = "2px solid green";
            }
            else{
                alert("Password does not match");
                isvalid=false;
            }
        
            if(isvalid==True){
                window.location.href("MCQ.html")
            }
        }       
