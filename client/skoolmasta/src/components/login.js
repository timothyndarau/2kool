import React, { useState } from 'react';
import '../App.css'; // Import the CSS file

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });
            if (response.ok) {
                // Login successful
                console.log('Login successful');
            } else {
                const data = await response.json();
                setError(data.error || 'Login failed');
            }
        } catch (error) {
            setError('An error occurred');
            console.error('Error occurred:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
                {loading && <p>Loading...</p>}
                {error && <p className="error">{error}</p>} {/* Apply error class */}
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;
