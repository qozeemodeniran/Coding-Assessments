const crypto = require('crypto');

// The `aes-256-cbc` algorithm requires a 256-bit (32-byte) key and a 128-bit (16-byte) IV
const algorithm = 'aes-256-cbc';
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);

// The text to be encrypted
const text = 'Hello, Hacker!';

// Encrypt the text
const cipher = crypto.createCipheriv(algorithm, key, iv);
let encrypted = cipher.update(text, 'utf8', 'hex');
encrypted += cipher.final('hex');

console.log(`Encrypted text: ${encrypted}`);

// Decrypt the text
const decipher = crypto.createDecipheriv(algorithm, key, iv);
let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');

console.log(`Decrypted text: ${decrypted}`);