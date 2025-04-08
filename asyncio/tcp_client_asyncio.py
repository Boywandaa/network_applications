import asyncio

async def client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888	)

    #prompt for message
    message = input("Enter message: ")

    #send the message
    writer.write(message.encode())

    print(f"sent {message}")

    #receive echo on steroids
    data = await reader.read(100)

    print(f"received {data.decode()}")

    print("closing connection")

    writer.close()

asyncio.run(client())
