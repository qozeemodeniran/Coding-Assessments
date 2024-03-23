const express = require('express');
const xss = require('xss');

const app = express();

app.use(express.json());

app.post('/data', (req, res) => {
    // Get user-supplied data
    const userData = req.body.data;

    // Apply input validation (this is a simple example, you may need more complex validation depending on your use case)
    if (typeof userData !== 'string') {
        return res.status(400).send('Invalid data');
    }

    // Apply output encoding
    const safeData = xss(userData);

    // Use the safe data (e.g., store it in a database, display it on a webpage, etc.)
    // ...

    res.send('Data received');
});

app.listen(3000, () => console.log('Server running at http://localhost:3000'));