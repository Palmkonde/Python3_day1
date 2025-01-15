import socket
import sys

HOST = '0.0.0.0' 
PORT = 50005
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as msg:
    s = None
    print(f"Error to creating socket: {msg}")

try:
    s.bind((HOST, PORT))
    s.listen()
except OSError as msg:
    print("Error waiting for connection!")
    s.close()
    s = None

if s is None:
    print('could not open socket')
    sys.exit(1)

conn, addr = s.accept()

with conn:
    print('Connected by', addr)
    data = conn.recv(1024)
    print(data)

    conn.send(b'Hello from server!')
print("Server finish!")
