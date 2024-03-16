import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./App.css";
import { NavLink } from "react-router-dom";
import logo from "./logo.png";

function Signup() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [usertype, setUsertype] = useState("user");
    const [phone, setPhone] = useState("");
    const [address, setAddress] = useState("");
    const [error, setError] = useState(""); 
  
    const handleSignup = async () => {
      try {
        const response = await fetch("/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include", // Include cookies in the request
          body: JSON.stringify({ username, password, email, usertype, phone, address}),
        });
  
        if (response.ok) {
          const result = await response.json();
          console.log(result.message); // Check for the success message
          navigate("/calendar"); // Redirect or handle state change
        } else {
          // Handle signup failure
          const result = await response.json();
          setError(result.error || "Signup failed"); // Set the error message
        }
      } catch (error) {
        console.error("Signup error:", error);
        setError("An unexpected error occurred"); // Set a generic error message
      }
    };
  
    return (
      <div >
        <NavLink to="/">
            <img src={logo} className="App-logo"  alt="Fostr" />
          </NavLink>
        <h2>Signup</h2>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <form>
          <label>
            Username:
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
          </label>
          <br />
          <label>
            Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </label>
          <br />
          <label>
            Email:
            <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
          </label>
          <br />
          <label>
            Usertype:
            <select value={usertype} onChange={(e) => setUsertype(e.target.value)}>
              <option value="user">Artist</option>
              <option value="admin">Admin</option>
            </select>
          </label>
          <br />
          <label>
            Phone:
            <input type="text" value={phone} onChange={(e) => setPhone(e.target.value)} />
          </label>
          <br />
          <label>
            Address:
            <input type="text" value={address} onChange={(e) => setAddress(e.target.value)} />
          </label>
          <br />
          <button type="button" onClick={handleSignup}>
            Signup
          </button>
        </form>
      </div>
    );
  }
  
  export default Signup;