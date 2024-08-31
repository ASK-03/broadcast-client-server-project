import socket
import threading

SERVER_PORT = 12345

# Create a TCP/IP socket to connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
client.connect(('127.0.0.1', SERVER_PORT))

def receive_messages():
    """
    Function to handle receiving messages from the server.
    It continuously listens for incoming messages from the server and
    prints them to the console.
    """
    while True:
        try:
            # Receive message from the server
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # Handle any errors that may occur (e.g., server disconnection)
            print("Connection closed by the server.")
            break

# Start a separate thread to handle receiving messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages to the server
while True:
    # Input message from the user
    message = input("You: ")
    
    # Send the message to the server
    client.send(message.encode('utf-8'))
