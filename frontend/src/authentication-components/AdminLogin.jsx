import { useState } from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/MasomoLMS-auth.svg';
import './auth.css';

export default function AdminLogin() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5000/admin-login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
      
      if (response.ok) {
        // Extract admin ID from response
        const data = await response.json();
        const adminId = data.admin_id;
        
        // Store admin ID in localStorage
        localStorage.setItem('adminId', adminId);

        // Redirect to admin dashboard or any other page upon successful login
        window.location.href = '/dashboard';
      } else {
        const data = await response.json();
        setError(data.message);
      }
    } catch (error) {
      console.error('Error logging in:', error);
      setError('Error logging in. Please try again later.');
    }
  };

  return (
    <div className="auth-container">
      <img src={logo} alt="MasomoLMS Logo" className="auth-logo" />
      <h2>Admin Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="auth-form-group">
          <label htmlFor="email">Email Address</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter your email address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="auth-form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit" className="auth-primary-button">Login</button>
      </form>
      {error && <p className="error">{error}</p>}
      <p>Don&apos;t have an account? <Link to="/admin-sign-up">Sign Up</Link></p>
    </div>
  );
}
