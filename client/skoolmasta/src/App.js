import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Login from './components/login';
import Signup from './components/signup';
import AdminDashboard from './components/AdminDashboard';
import AttemptedBorrows from './components/AttemptedBorrows';
import Input from './components/input';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/admin/dashboard" element={<AdminDashboard />} />
          <Route path="/admin/attempts" element={<AttemptedBorrows />} />
          <Route path="/input" element={<Input />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
