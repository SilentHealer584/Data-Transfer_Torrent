import socket
import rsa

public_keys = {}

s = socket.socket()         
print("Socket successfully created")
 
port = 42069             
 
s.bind(('', port))         
print("socket binded to %s" % (port)) 
 
s.listen(5)     
print("socket is listening")

def send(c, addr, content):
    c.send(rsa.encrypt(content.encode(), public_keys[addr]))

while True: 
    c, addr = s.accept()     
    print('Established connection with', addr)

    # Initiate Handshake
    public_key_str = c.recv(2048).decode()
    public_key = rsa.PublicKey.load_pkcs1(public_key_str)
    public_keys[addr] = public_key

    print(public_keys[addr])

    userinput = input("Message: ")

    c.send(rsa.encrypt(userinput.encode(), public_keys[addr]))

    c.close()
    break
