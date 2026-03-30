import React, { useState, useEffect } from 'react';
import './CyberDashboard.css';

function CyberDashboard() {
    const [servers, setServers] = useState([0, 0, 0, 0, 0]);

    // Initial state fetching
    useEffect(() => {
        fetch('/state')
            .then(res => res.json())
            .then(data => setServers(data.state))
            .catch(err => console.error("Backend connect nahi ho raha:", err));
    }, []);

    const patchServer = (index) => {
        fetch('/step', {
            method: 'POST',
            body: JSON.stringify({ action: index }),
            headers: { 'Content-Type': 'application/json' },
        })
            .then(res => res.json())
            .then(data => setServers(data.state));
    };

    return (
        <div className="dashboard cyberpunk-theme">
            <h1 className="glitch">NEUTRAL-SHIELD MONITOR</h1>
            <div className="server-container">
                {servers.map((status, index) => (
                    <div key={index} className={`server-box status-${status}`}>
                        <h3>SERVER_0{index + 1}</h3>
                        <div className="status-indicator">
                            {status === 0 ? "SAFE" : status === 1 ? "WARNING" : status === 2 ? "ATTACK" : "DOWN"}
                        </div>
                        <button className="patch-btn" onClick={() => patchServer(index)}>
                            EXECUTE PATCH
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default CyberDashboard;