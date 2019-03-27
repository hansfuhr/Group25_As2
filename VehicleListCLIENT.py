import socket
def client():
    host = socket.gethostname()
    port = 3262
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = ""

    while message.lower().strip()!= 'exit':
        data = client_socket.recv(1024).decode()
        print('Autobot: '+data)
        message = input("User: ")
        client_socket.send(message.encode())
    client_socket.close()

if __name__ == '__main__':
    client()