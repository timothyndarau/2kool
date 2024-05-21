import React, { useState, useEffect } from 'react';
import '../App.css';

const AdminDashboard = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [teachers, setTeachers] = useState([]);
    const [students, setStudents] = useState([]);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        setLoading(true);
        try {
            const response = await fetch('http://localhost:3000/admin/dashboard');
            if (response.ok) {
                const data = await response.json();
                setTeachers(data.teachers);
                setStudents(data.students);
                setItems(data.items);
            } else {
                setError('Failed to fetch data');
            }
        } catch (error) {
            setError('An error occurred');
            console.error('Error occurred:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="admin-dashboard-container">
            <h2>Admin Dashboard</h2>
            {loading && <p>Loading...</p>}
            {error && <p className="error">{error}</p>}
            {/* Display data fetched */}
            <h3>Teachers</h3>
            <ul>
                {teachers.map((teacher) => (
                    <li key={teacher.id}>{teacher.name}</li>
                ))}
            </ul>
            <h3>Students</h3>
            <ul>
                {students.map((student) => (
                    <li key={student.id}>{student.name}</li>
                ))}
            </ul>
            <h3>Items</h3>
            <ul>
                {items.map((item) => (
                    <li key={item.id}>{item.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default AdminDashboard;
