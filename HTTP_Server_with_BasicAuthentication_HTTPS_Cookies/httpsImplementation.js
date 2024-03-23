const https = require('https');
const fs = require('fs');
const config = require('./config.json');

// Define the path to your SSL/TLS certificate and private key
const options = {
    // openssl genpkey -algorithm RSA -out private-key.pem -aes256
    key: fs.readFileSync('private-key.pem'),
    //passphrase: 'testing',
    passphrase: config.passphrase,

    // openssl req -new -key private-key.pem -x509 -days 365 -out certificate.pem
    cert: fs.readFileSync('certificate.pem')
};

// Define the port the server will listen on
const PORT = 443;

// Create an HTTPS server
const server = https.createServer(options, (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, Hacker!\nYou are now connected to a secure server\n');
});

// Start the server and listen on the specified port
server.listen(PORT, () => {
    console.log(`Server running at https://localhost:${PORT}/`);
});