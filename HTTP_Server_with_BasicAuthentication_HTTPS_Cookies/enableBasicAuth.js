const http = require('http');
const atob = require('atob'); // Used for decoding base64-encoded strings

// Define the username and password for basic authentication
const username = 'admin';
const password = 'password';

// Define the port the server will listen on
const PORT = 3000;

// Create an HTTP server
const server = http.createServer((req, res) => {
    // Extract the 'Authorization' header from the request
    const authHeader = req.headers.authorization;

    // Check if the 'Authorization' header is present
    if (authHeader) {
        // Extract the base64-encoded credentials from the 'Authorization' header
        const encodedCredentials = authHeader.split(' ')[1];

        // Decode the base64-encoded credentials
        const decodedCredentials = atob(encodedCredentials);

        // Split the decoded credentials into username and password
        const [receivedUsername, receivedPassword] = decodedCredentials.split(':');

        // Check if the received username and password match the expected credentials
        if (receivedUsername === username && receivedPassword === password) {
            // If the credentials are valid, allow access to the protected resource
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end('Authentication successful\n');
        } else {
            // If the credentials are invalid, send a 401 Unauthorized response
            res.writeHead(401, { 'WWW-Authenticate': 'Basic realm="Restricted Access"' });
            res.end('401 Unauthorized\n');
        }
    } else {
        // If the 'Authorization' header is not present, send a 401 Unauthorized response
        res.writeHead(401, { 'WWW-Authenticate': 'Basic realm="Restricted Access"' });
        res.end('401 Unauthorized\n');
    }
});

// Start the server and listen on the specified port
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});