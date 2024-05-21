import React, { useState } from 'react';
import '../App.css';

const Input = () => {
    const [itemName, setItemName] = useState('');
    const [quantity, setQuantity] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await fetch('http://localhost:3000/input', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ itemName, quantity }),
            });
            if (response.ok) {
                // Input successful
                console.log('Input successful');
            } else {
                const data = await response.json();
                setError(data.error || 'Input failed');
            }
        } catch (error) {
            setError('An error occurred');
            console.error('Error occurred:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form className="input-form" onSubmit={handleSubmit}>
            <input type="text" value={itemName} onChange={(e) => setItemName(e.target.value)} placeholder="Item Name" className="input-field" />
            <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} placeholder="Quantity" className="input-field" />
            {loading && <p>Loading...</p>}
            {error && <p className="error-message">{error}</p>}
            <button type="submit" className="submit-button">Add Item</button>
        </form>
    );
};

export default Input;
