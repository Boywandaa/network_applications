from socket import *

def main():

    #create a socket for the server
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    #bind address to the socket
    server_address = ("0.0.0.0", 12580)
    serverSocket.bind(server_address)

    print(f"server is running on {server_address}")


    while True:
        

        #receive messages from clients
        message, client_addr = serverSocket.recvfrom(2048)

        print(f"received: \" {message.decode()} \" from client running on {client_addr}")
        

        #process the message
        modifiedMessage = message.decode().upper()
        print(f"processing.....")

        #send the response
        serverSocket.sendto(modifiedMessage.encode(), client_addr)
        print(f"sent \" {modifiedMessage} \" to client running on {client_addr}")
        print()
        print(".........................................................")

    #close the server socket
    serverSocket.close()

main()
