# Data-Transfer_Torrent

Hello World!

I present to you a data transfer system based on Python's Socket Module.
It makes use of my own [RSA Module](https://github.com/SilentHealer584/RSA-i-guess) to safely encrypt the communicated data.

Refer to my RSA Module's README for download and setup instructions.

##How does it work?

1. The Client script generate two keys, one public, one private thanks to the [rsa_i_guess]((https://github.com/SilentHealer584/RSA-i-guess)) module.
2. The Client connects to the Server and sends it the unecrypted public key (This is the only bad part).
3. The Server receives the key, encrypts a message and sends it to the Client.
4. The client decrypts the message.


There are some flaws in the way the key is communicated (unencrypted and cut) which can be fixed. Don't use this for any serious communication purposes.
This is more of a demo.
