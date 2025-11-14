import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 3003))
server_socket.listen()

print('Server is runnning on localhost:3003')

while True:
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}')
    request = client_socket.recv(1024).decode()
    if (not request) or ('favicon.ico' in request):
        client_socket.close()
        continue
    request_line = request.splitlines()[0]

    roll = random.randint(1,6)
    response_body = f'{request_line}\n{roll}\n'

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}\n")
    
    client_socket.sendall(response.encode())
    client_socket.close()