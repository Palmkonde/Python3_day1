import socket
import sys

HOST = None 
PORT = 50005
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    print(res)
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue

    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        print("Error waiting for connection!")
        s.close()
        s = None
        continue
    break

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
