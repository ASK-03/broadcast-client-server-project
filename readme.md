# Broadcast Messaging System

This project implements a simple broadcast messaging system using Python's socket programming. It allows multiple clients to connect to a server, and any message sent by one client is broadcasted to all other connected clients in real time.

**(This project is designed as a learning exercise to demonstrate basic socket programming and multi-threading in Python. It is not intended to be used as a full-fledged messaging server for production environments.)**

## Features

- **Multi-Client Support:** The server can handle multiple clients simultaneously, enabling group communication.
- **Real-Time Message Broadcasting:** Messages sent by any connected client are instantly broadcasted to all other clients.
- **Threaded Client Handling:** Each client connection is managed in a separate thread, ensuring smooth and efficient communication without blocking.
- **Simple Setup:** The server and client scripts are straightforward to run, with minimal configuration required.
- **Connection Management:** The server manages active connections, automatically removing clients that disconnect.

## Dependencies

- **Python3**: Ensure that you have Python 3 installed on your system. You can download and install Python 3 from the official Python website: https://www.python.org.
- **pip**: pip is the package installer for Python. It is usually installed by default when you install Python. However, make sure you have pip installed and it is up to date. You can check the version of pip by running the following command:

  ```
  pip --version
  ```

  (Use this command to check, if pip is installed correctly)

  ```
  pip install -r requirements.txt
  ```

  After cloning the repository, to install all the requirements at once.

## Installation

To install and use carrer-scraper, follow the steps given below:

- Fork the carrer-scraper repository by clicking the "Fork" button at the top right corner of the repository page. This will create a copy of the repository under your GitHub account.

- Clone the forked repository to your local machine:

  ```
  git clone https://github.com/{YOUR-USERNAME}/broadcast-client-server-project
  ```

- Navigate to the project directory:
  ```
  cd broadcast-client-server-project
  ```
- Install the necessary Python packages by running the following command:
  ```
  pip install -r requirements.txt
  ```
- Navigate to the files

  ```
  cd broadcast-client-server-project
  ```

## Setup Instructions

### 1. Run the server

```
bash
python3 server.py
```

**(The server will now listen for incoming connections on port `12345`)**

### 2. Run the Client

```
bash
python3 client.py
```

**Tip: Start some more server in the same way in different terminals.**

**(The client will connect to the server running on `127.0.0.1:12345`)**

### 3. Messaging

Once connected, any message sent by one client will be broadcasted to all other connected clients. Type exit to disconnect a client from the server.

## Troubleshooting

- **Port Conflicts:** If port **12345** is in use, modify the `SERVER_PORT` in both `server.py` and `client.py`.
- **Connection Issues:** Ensure that the server is running and reachable from the client.

## Future Enhancements

While this project serves as a basic implementation of a broadcast messaging system, there are several potential enhancements that could be made to extend its functionality and robustness:

1. **User Authentication:**

   - Implement a simple authentication mechanism to verify users before allowing them to join the chat. This could include usernames and passwords or even OAuth for more secure access.

2. **Message Encryption:**

   - Add encryption to the messages being transmitted between clients and the server to ensure secure communication, especially if the system is used over a public network.

3. **Private Messaging:**

   - Introduce the ability for clients to send private messages to specific users instead of broadcasting to all connected clients.

4. **Graphical User Interface (GUI):**

   - Develop a simple GUI using libraries like Tkinter or PyQt to make the client application more user-friendly.

5. **Message History:**

   - Implement a feature to store and retrieve message history so that new clients can see previous conversations when they connect.

6. **Enhanced Error Handling:**

   - Improve error handling to manage unexpected disconnections, network issues, and other potential runtime errors more gracefully.

7. **Client Disconnect Notification:**

   - Notify all clients when a user disconnects from the server, enhancing the chat experience with real-time status updates.

8. **File Transfer Support:**

   - Add support for sending and receiving files between clients through the server.

9. **Server-Client Heartbeat Mechanism:**

   - Implement a heartbeat mechanism to monitor the connection status of clients and remove inactive ones from the clients list automatically.

10. **Scalability:**

    - Explore ways to scale the server to handle more clients, possibly by implementing load balancing or distributed server architecture.

11. **Cross-Platform Compatibility:**
    - Ensure that the client and server can run smoothly on different operating systems, such as Windows, macOS, and Linux.

These enhancements could significantly improve the functionality and usability of the messaging system, making it more robust, secure, and feature-rich.

## Contributions

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## Author

[Abhishek Singh Kushwaha](https://ask-03-portfolio.vercel.app/)
