const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send(`<pre>${JSON.stringify(req.headers, null, 2)}</pre>`);
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));