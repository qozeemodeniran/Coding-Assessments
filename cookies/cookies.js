const http = require('http');

// Function to set cookies in the HTTP response headers
function setCookies(res) {
    // Set cookies with key-value pairs
    res.setHeader('Set-Cookie', [
        'user_id=123456; Max-Age=3600', // Cookie with a maximum age of 1 hour (in seconds)
        'session_id=abcdefg; Path=/; Secure; HttpOnly' // Secure and HttpOnly cookie with a specified path
    ]);
}

// Function to read cookies from the HTTP request headers
function readCookies(req) {
    // Extract cookies from the 'Cookie' header
    const cookieHeader = req.headers.cookie;
    if (cookieHeader) {
        // Split cookie header string into individual cookies
        const cookies = cookieHeader.split('; ');

        // Parse each cookie into key-value pairs
        const parsedCookies = {};
        cookies.forEach(cookie => {
            const [key, value] = cookie.split('=');
            parsedCookies[key] = value;
        });

        return parsedCookies;
    } else {
        return {};
    }
}

// Create an HTTP server
const server = http.createServer((req, res) => {
    // Set cookies in the response headers
    setCookies(res);

    // Read cookies from the request headers
    const cookies = readCookies(req);

    // Send a response with the cookies received
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(`Received cookies: ${JSON.stringify(cookies)}`);
});

// Define the port for the HTTP server to listen on
const PORT = 3000;

// Start the HTTP server
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});