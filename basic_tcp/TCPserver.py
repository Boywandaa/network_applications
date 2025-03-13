import socket

#create a tcp socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind an ip address to the socket
serverAddress = (("127.0.0.1", 12580))
serverSocket.bind(serverAddress)
print(f"server is running on {serverAddress}")

#trigger the server to start listening for incoming connections
serverSocket.listen(3)

while True:
    #establish a new client socket 
    connection_socket, client_addr = serverSocket.accept()

    #recieve messages from the established client connection
    message, _ = connection_socket.recv(2048)

    if quit == message:
        break

    print(f"received {message.decode()} from client running on {client_addr}")

    #process the client message
    modifiedMessage = message.decode().upper()

    #send the message to the client
    connection_socket.send(modifiedMessage.encode())

    print()

serverSocket.close()
    