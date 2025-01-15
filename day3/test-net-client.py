import socket

HOST = '127.0.0.1'
PORT = 50005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    while True:
        message_sending = input("Enter a message: ")
        
        # Exit the connect
        if message_sending.lower() == "exit":
            break

        s.send((message_sending + "\n").encode())
        print("Message sent!")
        print("Waiting for server...")

        message_received = ""
        while True:
            data = s.recv(1024)
            if data:
                print('Received data chunk from server: ', repr(data))
                message_received += data.decode()
                if message_received.endswith("\n"):
                    print(f"Server: {message_received}")
                    break
            else:
                print("Connection lost!")
                break
        if not message_received:
            break
        

print("Client finished")