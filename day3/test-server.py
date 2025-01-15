import socket

HOST = '0.0.0.0'
PORT = 50005
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)


while True:
    conn, addr = s.accept()
    with conn:
        print('Connection accepted from ', addr)

        while True:
            message_received = ""
            while True:
                data = conn.recv(1024)
                if data:
                    print('Received data chunk from client: ', repr(data))
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print("\nConnection lost!")
                    break

            if message_received:
                print("Client: ", message_received)

                message_sending = input("Enter a message: ")
                conn.send((message_sending + '\n').encode()) 
                print("Message sent!")
                print("Waiting for client...")
            
            else:
                print("Waiting for new client...")
                break

s.close()
print("Server finished")