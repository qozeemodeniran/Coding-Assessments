const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/submit-data', (req, res) => {
    const { username } = req.body;

    // Perform necessary operations with username (e.g., save to database)  
    // Connect to the database
    mongoose.connect('mongodb://localhost/mydatabase', {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        })
        .then(() => {
            console.log('Connected to the database');
        })
        .catch((error) => {
            console.error('Error connecting to the database:', error);
        });

    // Define the User schema
    const userSchema = new mongoose.Schema({
        username: String,
    });

    // Create the User model
    const User = mongoose.model('User', userSchema);
    const user = new User({ username });

    // Save username to databasea
    user.save()
        .then(() => {
            console.log('Username saved to database');
        })
        .catch((error) => {
            console.error('Error saving username to database:', error);
        });

    // For demonstration purposes, we'll simply echo the username back
    res.send(`Received username: ${username}`);
});

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});