Client-Server Chat Application

This project is a simple TCP-based client-server chat application using Python's socket library. It allows two users (one acting as the server and the other as the client) to exchange text messages over a network.

## Features
Client-Server Communication: The server listens for incoming client connections. Once a connection is established, the client and server can exchange messages.
Real-time Messaging: Both client and server can send and receive messages in real-time.
TCP Connection: Communication is done via a reliable TCP protocol ensuring proper delivery of messages.
Graceful Exit: Either the client or server can end the chat session by sending the message "bye".
## Requirements
Python 3.x
## How to Run
1. Server Side:
First, start the server on one machine or terminal. The server will wait for the client to connect.
* python server.py
You should see:

Server is waiting for a connection...
2. Client Side:
On another machine or terminal, run the client. The client will attempt to connect to the server.

python client.py
You should see:

Connected to the server.
3. Communication:
Once connected, the client and server can send messages back and forth via the terminal/command prompt.
To exit the chat, either party can type bye.

## Code Overview

Server (server.py):
Creates a TCP socket and binds it to the host and port.
Listens for incoming client connections.
Once a client connects, the server can send and receive messages until one party says "bye".
After the chat session ends, the server closes the connection.
Client (client.py):
Creates a TCP socket and connects to the server using the host and port.
Sends messages to the server and receives messages back.
Exits the chat when either party says "bye".
Example Interaction

## Server Terminal:

Server is waiting for a connection...
Got a connection from ('192.168.1.2', 54321)
Client: Hello, Server!
You: Hi there!
Client: How are you?
You: I’m doing well, thanks! How about you?
Client: I’m good too. Bye!
You: Bye!
Chat ended.

##Client Terminal:

Connected to the server.
You: Hello, Server!
Server: Hi there!
You: How are you?
Server: I’m doing well, thanks! How about you?
You: I’m good too. Bye!
Server: Bye!
Chat ended.
Enhancements

## You can extend this project with the following features:

Multi-client support: Use threading on the server to handle multiple clients concurrently.
GUI: Implement a graphical interface using tkinter or another framework for a more user-friendly chat experience.
Encryption: Add encryption to the communication for more secure message transmission.