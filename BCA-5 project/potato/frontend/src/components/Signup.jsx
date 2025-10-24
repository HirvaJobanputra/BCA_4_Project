import React, { useState } from "react";
import {
  createUserWithEmailAndPassword,
  signInWithPopup,
} from "firebase/auth";
import { auth, googleProvider } from "../firebase";
import emailjs from "@emailjs/browser";
import "../App.css";

function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [otp, setOtp] = useState("");
  const [generatedOtp, setGeneratedOtp] = useState("");
  const [step, setStep] = useState(1);

  // Send OTP
  const sendOtp = async (e) => {

    e.preventDefault();
    const otpCode = Math.floor(100000 + Math.random() * 900000).toString();
    setGeneratedOtp(otpCode);

    console.log("Generated OTP:", otpCode); // For debugging
    console.log("Email:", email); // For debugging
    try {
      await emailjs.send(
        "service_mnuvual",
        "template_644qs0i",
        { otp: otpCode, to_email: email },
        "NrCw6U8sj_KGIYsf1"
      );
      alert("OTP sent to your email!");
      setStep(2);
    } catch (error) {
      console.error("EmailJS error:", error);
      alert("Failed to send OTP. Try again.");
    }
  };

  // Verify OTP + signup in Firebase
  const verifyOtpAndSignup = async (e) => {
    e.preventDefault();
    if (otp === generatedOtp) {
      try {
        await createUserWithEmailAndPassword(auth, email, password);
        alert("Signup successful");
        // redirect to homepage
        window.location.href = "./ManageMenu";
      } catch (error) {
        console.error("Firebase error:", error);
        alert(error.message);
      }
    } else {
      alert("Invalid OTP ");
    }
  };

  // Google Signup/Login
  const googleSignup = async () => {
    try {
      await signInWithPopup(auth, googleProvider);
      alert("Google Signup successful ");
      window.location.href = "./ManageMenu";
    } catch (error) {
      console.error("Google login error:", error);
      alert(error.message);
    }
  };

  return (
    <div className=" text-center p-6 signup-page">
      
<div className="glass-effect">
    {step === 1 && (
        <form className="flex flex-col gap-3 mt-4" onSubmit={sendOtp}>
         <h1 className="text-2xl font-bold title">Signup</h1>
          <input
            type="email"
            placeholder="Email"
            className="input-field"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="input-field"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button className="btn" type="submit">
            Send OTP
          </button>
        </form>
      )}

      {step === 2 && (
        <form className="flex flex-col gap-3 mt-4" onSubmit={verifyOtpAndSignup}>
          <input
            type="text"
            placeholder="Enter OTP"
            className="border p-2 rounded mt-2"
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
            required
          />
          <button className="bg-blue-500 text-white py-2 rounded" type="submit">
            Verify & Signup
          </button>
        </form>
      )}

      <div className="mt-4">
        <p>Or sign up with:</p>
        <button
          className="btn"
          onClick={googleSignup}
        >
          Google
        </button>
      </div>
    </div>   
  </div>
 );
}
export default Signup;