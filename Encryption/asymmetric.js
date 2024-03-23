const crypto = require('crypto');

// Generate an RSA keypair with a key length of 2048 bits
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
});

// The text to be encrypted
const text = 'Hello, Hacker!';

// Encrypt the text using the public key
const encrypted = crypto.publicEncrypt(publicKey, Buffer.from(text));

console.log(`Encrypted text: ${encrypted.toString('base64')}`);

// Decrypt the text using the private key
const decrypted = crypto.privateDecrypt(privateKey, encrypted);

console.log(`Decrypted text: ${decrypted.toString()}`);