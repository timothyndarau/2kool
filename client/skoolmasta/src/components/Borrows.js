import React, { useState, useEffect } from 'react';

const Borrow = () => {
    const [items, setItems] = useState([]);
    const [selectedItem, setSelectedItem] = useState(null);
    const [quantity, setQuantity] = useState(1);
    const [message, setMessage] = useState('');

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const response = await fetch('/api/items');
                const data = await response.json();
                setItems(data);
            } catch (error) {
                setMessage('Error fetching items.');
            }
        };
        fetchItems();
    }, []);

    const handleBorrow = async () => {
        try {
            const response = await fetch('http://localhost:3000/borrow', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ item_id: selectedItem.id, quantity })
            });
            const data = await response.json();
            setMessage(data.message);
        } catch (error) {
            setMessage('Error borrowing item.');
        }
    };

    return (
        <div>
            <h2>Borrow Items</h2>
            <div>
                <label>Select Item:</label>
                <select onChange={(e) => setSelectedItem(items.find(item => item.id === parseInt(e.target.value)))}>
                    <option value="">Select an item</option>
                    {items.map(item => (
                        <option key={item.id} value={item.id}>
                            {item.name}
                        </option>
                    ))}
                </select>
            </div>
            <div>
                <label>Quantity:</label>
                <input
                    type="number"
                    value={quantity}
                    onChange={(e) => setQuantity(e.target.value)}
                    min="1"
                />
            </div>
            <button onClick={handleBorrow}>Borrow</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default Borrow;
