import socket


def _run_server(SERVER_HOST: str, SERVER_PORT: int, run_route):
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    while True:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()
        print(f"getting request from {client_address}")

        # Get the client request
        request = client_connection.recv(1024).decode()

        # Send HTTP response
        client_connection.sendall(run_route(request).encode())
        client_connection.close()

    server_socket.close()
