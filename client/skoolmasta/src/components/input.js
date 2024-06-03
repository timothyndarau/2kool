import React, { useState } from "react";
import '../App.css';

const Signup = () => {
    const [itemName, setItemName] = useState("");
    const [quantity, setQuantity] = useState("");
    const [description, setDescription] = useState(""); // New state for description
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      setLoading(true);
      setError(""); // Clear any previous error
  
      try {
        const response = await fetch('http://localhost:5000/input', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ itemName, quantity, description }), // Include description
        });
  
        if (!response.ok) {
          const data = await response.json();
          throw new Error(data.error || 'Failed to add item');
        }
  
        const data = await response.json();
        console.log('Item added successfully:', data.message);
  
        // Clear the form fields after successful submission
        setItemName("");
        setQuantity("");
        setDescription(""); // Clear the description
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
  
    return (
      <div className="add-to-inventory-container">
        <h2>Add to Inventory</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={itemName}
            onChange={(e) => setItemName(e.target.value)}
            placeholder="Item Name"
            disabled={loading}
            required
          />
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            placeholder="Quantity"
            disabled={loading}
            required
          />
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Description" // New input for description
            disabled={loading}
            required
          />
          {loading && <p>Loading...</p>}
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <button type="submit" disabled={loading}>
            {loading ? 'Adding...' : 'Add to Inventory'}
          </button>
        </form>
      </div>
  
  );
};

export default Signup;
