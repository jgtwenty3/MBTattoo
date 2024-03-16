import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './index.css';
import App from './App';
import Login from './Login';
import Signup from './Signup';
import Calendar from './Calendar';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <Router>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/login" element={<Login />} />
      <Route path = "/sign-up" element = {<Signup/>}/>
      <Route path = "/calendar" element = {<Calendar/>}/>
    </Routes>
  </Router>,
  document.getElementById('root')
);

reportWebVitals();