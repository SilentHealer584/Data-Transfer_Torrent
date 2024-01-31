import socket
import rsa

public_key, private_key = rsa.newkeys(2048)
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 42069               
 
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
 
# Initiate Handshake
public_key_str = rsa.PublicKey.save_pkcs1(public_key).decode()
s.send(public_key_str.encode())

print(rsa.decrypt(s.recv(8192), private_key).decode())

# close the connection 
s.close()
