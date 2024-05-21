import React, { useState, useEffect } from 'react';
import '../App.css';

const AttemptedBorrows = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [attemptedBorrows, setAttemptedBorrows] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        setLoading(true);
        try {
            const response = await fetch('http://localhost:3000/admin/attempts');
            if (response.ok) {
                const data = await response.json();
                setAttemptedBorrows(data.attemptedBorrows);
            } else {
                setError('Failed to fetch attempted borrows');
            }
        } catch (error) {
            if (error.name === 'SyntaxError') {
                setError('Invalid JSON response');
            } else {
                setError('An error occurred');
                console.error('Error occurred:', error);
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="attempted-borrows-container">
            <h2>Attempted Borrows</h2>
            {loading && <p>Loading...</p>}
            {error && <p className="error">{error}</p>}
            {/* Display attempted borrows */}
            <ul>
                {attemptedBorrows.map((borrow) => (
                    <li key={borrow.id}>{borrow.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default AttemptedBorrows;
