const express = require('express');
const session = require('express-session');
const csrf = require('csurf');

const app = express();

// Enable session management
app.use(session({
    secret: 'my secret', // Replace this with a real secret in production
    resave: false,
    saveUninitialized: true,
}));

// Enable CSRF protection
app.use(csrf());

app.get('/form', (req, res) => {
    // Render the form, including the CSRF token
    res.send(`
        <form action="/process" method="POST">
            <input type="hidden" name="_csrf" value="${req.csrfToken()}">
            <!-- Other form fields go here -->
            <button type="submit">Submit</button>
        </form>
    `);
});

app.post('/process', (req, res) => {
    // If we're here, the CSRF token was valid and the request is safe
    res.send('Data processed');
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));