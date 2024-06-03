import React, { useState, useEffect } from 'react';
import '../App.css';

const AttemptedBorrows = () => {
  const [attemptedBorrows, setAttemptedBorrows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchAttemptedBorrows = async () => {
      try {
        const response = await fetch('http://localhost:5000/admin/attempts');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setAttemptedBorrows(data.attempted_borrows);
        setLoading(false);
      } catch (error) {
        setError("Failed to fetch data");
        setLoading(false);
      }
    };

    fetchAttemptedBorrows();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  if (!attemptedBorrows || attemptedBorrows.length === 0) {
    return <p>No attempted borrows found</p>;
  }

  return (
    <div className="attempted-borrows-container">
      <h2>Attempted Borrows</h2>
      <ul>
        {attemptedBorrows.map((attempt) => (
          <li key={attempt.id}>
            User ID: {attempt.user_id}, Item ID: {attempt.item_id}, Returned: {attempt.returned.toString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AttemptedBorrows;
