import React, { useState } from 'react';
import '../App.css'; // Import the CSS file

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Form validation
        if (!username.trim() || !password.trim()) {
            setError('Please enter both username and password.');
            return;
        }

        setLoading(true);

        try {
            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            // Check if response is okay
            if (response.ok) {
                const responseData = await response.json(); // Parse JSON response
                console.log('Parsed Response Data:', responseData);
                // Further processing of parsed data...
                console.log('Login successful');
                setUsername('');
                setPassword('');
                setError('');
            } else {
                // Handle non-200 status code
                const data = await response.json();
                setError(data.error || 'Login failed');
            }
        } catch (error) {
            // Handle fetch or parsing errors
            setError('An error occurred. Please try again later.');
            console.error('Error occurred:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username:</label>
                <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                />
                <label htmlFor="password">Password:</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                />
                {loading && <p>Loading...</p>}
                {error && <p className="error">{error}</p>}
                <button type="submit" disabled={loading}>
                    {loading ? 'Logging in...' : 'Login'}
                </button>
            </form>
        </div>
    );
};

export default Login;
