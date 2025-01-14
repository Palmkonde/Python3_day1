import socket

HOST = 'localhost'    # The remote host
PORT = 50005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hi from client!')
    data = s.recv(1024)
print('Received', repr(data))