import asyncio
import hashlib


clients = {}

#handle client connection
async def handler_client(reader, writer):
    #get clients address
    addr = writer.get_extra_info('peername')

    #generate 8-digit SHA1 hash for client id
    client_id = hashlib.sha1(addr[1].encode()).hexdigest()[:8]
    print(f"Connected by {addr} (ID: {client_id})")

    clients[client_id] = writer

    while True:
        #read data from client 
        data = await reader.read(1000)

        if not data:
            print(f"client {client_id} disconnected")
            break

        message = data.decode()

        print(f"received {message} from {client_id}")
        if message == "quit":
            break
        
        #format message with client id
        formatted_message = f"{client_id} : {message}"

        # Broadcast message to all clients
        await broadcast_message(formatted_message, client_id)



   # Remove client from connected_clients and close connection
    if client_id in clients:
        del clients[client_id] 

    print(f"Closing connection with {client_id}")
    writer.close()        
    await writer.wait_closed()
    
# Broadcast message to all connected clients
async def broadcast_message(message, sender_id=None):
    for client_id, writer in clients.items():
        writer.write(message.encode())
        await writer.drain()
        print(f"Sent to {client_id}: {message}")
       

async def main():
    address = input("Enter server address: ").strip()
    port = int(input("Enter server port: ").strip())

    server = await asyncio.start_server(handler_client, address , port)
    addr = server.sockets[0].getsockname()

    print(f"Server listening on {addr}"	)

    async with server:
        await server.serve_forever()

asyncio.run(main())
    