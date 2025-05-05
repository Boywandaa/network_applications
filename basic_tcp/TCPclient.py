import socket
import time

#create the client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#establish a connection to a server
serverAddress = ("127.0.0.1", 12580)
clientSocket.connect(serverAddress)

while True:
    
    #send messages to the server
    message = input("enter a message: ")

    clientSocket.send(message.encode())
    print(f"sent {message} to server running on {serverAddress}")

    #receive the response from the server
    message = clientSocket.recv(2048)
    print(f"received {message.decode()} from server running on {serverAddress}")

    print()

clientSocket.close()