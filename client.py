import socket
import rsa_i_guess as rig

# Generate public and private keys
public, private = rig.key_gen(2048)

# Establich connection
s = socket.socket()         
s.connect(('127.0.0.1', 42069)) 

# Share Public Key
s.send(str(public[1]).encode())

# Decrypt received message with private key
print(rig.decrypt(int(s.recv(8192).decode()), private))

#Close connections
s.close()
