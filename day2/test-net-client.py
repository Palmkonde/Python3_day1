import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    print("Conntected to server!")
    
    while True:
        mssag