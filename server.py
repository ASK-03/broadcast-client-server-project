import socket
import threading

SERVER_PORT = 12345

# Create a TCP/IP socket to listen for incoming connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the localhost and a specific port (12345)
server.bind(('127.0.0.1', SERVER_PORT))

# Listen for incoming connections (maximum backlog of connections set to default)
server.listen()

# List to keep track of connected clients
clients = []

def handle_client(client_socket):
    """
    Function to handle communication with a connected client.
    It listens for incoming messages from the client and broadcasts
    the message to all other connected clients.
    """
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            
            # Broadcast the message to all other clients
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        except:
            # Handle client disconnection and remove client from the list
            clients.remove(client_socket)
            client_socket.close()
            break

# Main loop to accept incoming client connections
while True:
    print("Server is listening for connections...")
    
    # Accept a new client connection
    client, addr = server.accept()
    
    # Add the new client to the list of connected clients
    clients.append(client)
    
    print(f"New connection from {addr}")
    
    # Start a new thread to handle the communication with the connected client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
