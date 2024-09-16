import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name and port
    host = socket.gethostname()
    port = 12345
    
    # Connection to hostname on the port
    client_socket.connect((host, port))
    
    print("Connected to the server.")
    
    # Send and receive messages
    while True:
        # Send message to server
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))
        
        # Receive response from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}")
        
        if message.lower() == 'bye' or response.lower() == 'bye':
            print("Chat ended.")
            break
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
