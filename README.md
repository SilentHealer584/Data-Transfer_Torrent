# File-Transfer_Torrent

Hello World!

I present to you a data transfer system based on Python's Socket Module.
It makes use of Rsa to asymmetrically encrypt and decrypt data ensuring data protection.

How does it work?

1. The handshake
   - The Server is Started and The Client connects
   - The client Starts by communicating it's public key to the server to make it possible to encrypt messages only it can read
   - The Server receives the public key and assigns it to the client's IP in a dictionnary
   - The server finally sends a message to the Client to check It's connectivity and to make sure it can start communicating data