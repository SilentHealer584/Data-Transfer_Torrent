import socket
import rsa_i_guess as rig

message = "Hello World!"

# Set up server socket
c = socket.socket()
c.bind(('127.0.0.1', 42069))
c.listen(1)

# Wait for a client connection
c, addr = c.accept()

# Receive client's public key
public = int(c.recv(8192).decode())

c.send(str(rig.encrypt(str(message), [65537, public])).encode())

# Close connections
c.close()
