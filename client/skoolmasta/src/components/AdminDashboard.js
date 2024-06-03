import React, { useState, useEffect } from 'react';
import '../App.css';

const AdminDashboard = () => {
  const [attemptedBorrows, setAttemptedBorrows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchAttemptedBorrows = async () => {
      try {
        const response = await fetch('http://localhost:5000/admin/dashboard', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
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
    <div className="admin-dashboard">
      <h2>Borrowers History</h2>
      <ul>
        {attemptedBorrows.map((attempt) => (
          <li key={attempt.id}>
            User: {attempt.username}, Item: {attempt.item_name}, Borrowed At: {new Date(attempt.borrowed_at).toLocaleString()}, Returned: {attempt.returned.toString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminDashboard;
