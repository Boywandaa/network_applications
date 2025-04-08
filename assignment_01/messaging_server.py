import asyncio


#handle client connection
async def handler_client(reader, writer):
    #get clients address
    addr = writer.get_extra_info('peername')
    print(f"Connected by {addr}")

    while True:
        #read data from client 
        data = await reader.read(1000)

        if not data:
            print(f"client disconnected")
            break

        message = data.decode()

        print(f"received {message} from {addr}")
        if message == "quit":
            break
        
        #processing message
        processed_message = message.upper()

        writer.write(processed_message.encode())
        await writer.drain()
        print(f"sent: {processed_message}")

    print(f"Closing connection with {addr}")
    writer.close()
    await writer.wait_closed()
    

async def main():
    address = input("Enter server address: ").strip()
    port = int(input("Enter server port: ").strip())

    server = await asyncio.start_server(handler_client, address , port)
    addr = server.sockets[0].getsockname()

    print(f"Server listening on {addr}"	)

    async with server:
        await server.serve_forever()

asyncio.run(main())
    