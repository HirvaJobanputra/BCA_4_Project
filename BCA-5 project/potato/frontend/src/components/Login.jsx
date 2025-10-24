 import React, { useState } from "react";
  import { signInWithEmailAndPassword } from "firebase/auth"; 
 import { auth } from "../firebase"; 
 function Login()
  { 
    const [email, setEmail] = useState("");
     const [password, setPassword] = useState("");
      const loginUser = async () => {
         try 
         {
           await signInWithEmailAndPassword(auth, email, password); 
           alert("Login successful");
           }
            catch (error) {
               console.error("Login error:", error);
              alert(error.message);
            }};
       return ( 
       <div className="login-page"> 
       <div className="login-card glass-effect"> 
        <h1 className="title">Welcome Back</h1>
         <p className="subtitle">Login to continue</p>
          <input type="email" placeholder="Email" className="input-field" onChange={(e) => setEmail(e.target.value)} value={email} />
           <input type="password" placeholder="Password" className="input-field" onChange={(e) => setPassword(e.target.value)} value={password} /> 
           <button className="btn" onClick={loginUser}> Login </button>
            <p className="footer-text"> New here? <span className="link">Sign up</span> </p> </div> </div>
      );
} 
export default Login;