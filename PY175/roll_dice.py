import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()
    if not request or 'favicon.ico' in request:
        client_socket.close()
        continue

    request_line = request.splitlines()[0]
    http_method, path_and_params, _ = request_line.split(" ")
    path, params = path_and_params.split("?")

    params = params.split("&")
    params_dict = {}
    for param in params:
        key, value = param.split("=")
        params_dict[key] = value

    rolls = int(params_dict.get('rolls', '1'))
    sides = int(params_dict.get('sides', '6'))

    response_body = ("<html><head><title>Dice Rolls</title></head><body>"
                     f"<h1>HTTP Request Information:</h1>"
                     f"<p><strong>Request Line:</strong> {request_line}</p>"
                     f"<p><strong>HTTP Method</strong>: {http_method}</p>"
                     f"<p><strong>Path:</strong> {path}</p>"
                     f"<p><strong>Parameters:</strong> {params_dict}</p>"
                     "<h2>Rolls:</h2>"
                     "<ul>")


    for _ in range(rolls):
        roll = random.randint(1, sides)
        response_body += f"<li>Roll: {roll}</li>"
    
    response_body += "</ul></body></html>"

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}\n")

    client_socket.sendall(response.encode())
    client_socket.close()