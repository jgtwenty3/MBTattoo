import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import './App.css';
import { NavLink } from "react-router-dom";
import logo from "./logo.png";

function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
  
    const handleLogin = () => {
    
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      })
      .then(response => {
        // Handle response accordingly
        if (response.ok) {
          // Redirect to the calendar page if login is successful
          navigate("/calendar");
        } else {
          // Handle login failure
          console.error('Error logging in:', response.statusText); // Log error message from the response
        }
      })
      .catch(error => {
        // Handle errors from the fetch request
        console.error('Error logging in:', error);
      });
    };
       
    return (
      <div className="login-container"> 
        <NavLink to="/">
          <img src={logo} className="App-logo-sm" alt="MB" />
        </NavLink>
        <h1>Login</h1>
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
        <button className="login-btn" onClick={handleLogin}>Login</button>
      </div>
    );
}
  
export default Login;
