from socket import *

def main():

    #create a client socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #SERVER ADDRESS
    server_address = ("127.0.0.1", 12580)

    while True:

        #prompt  for a message from the stdin
        message = input("Enter a message: ")

        #send message to the server
        clientSocket.sendto(message.encode(), server_address)
        print(f"sent: {message} to server running on {server_address}")

        #receive message from server
        receivedMessage, server_addr = clientSocket.recvfrom(2048)
        print(f"received \"{receivedMessage.decode()}\" from a server running on {server_addr}")
        print()

    # #3close the client's socket
    # clientSocket.close()

main()