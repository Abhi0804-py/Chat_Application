import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name and port
    host = socket.gethostname()
    port = 12345
    
    # Bind to the port
    server_socket.bind((host, port))
    
    # Start listening for connections (allow up to 5 clients to connect)
    server_socket.listen(5)
    
    print("Server is waiting for a connection...")
    
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")
    
    # Send and receive messages
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Client: {message}")
        
        # Send response back to the client
        response = input("You: ")
        client_socket.send(response.encode('utf-8'))

        if message.lower() == 'bye' or response.lower() == 'bye':
            print("Chat ended.")
            break
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_server()
