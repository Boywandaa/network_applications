# file: async_http_server.py

import asyncio

async def handle_client(reader, writer):
    request = await reader.read(1024)
    message = request.decode()
    print(f"Received:\n{message}")

    response_body = '{"message": "Hello from Async HTTP Server!"}'
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{response_body}"
    )
    writer.write(response.encode())
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8080)
    print("Serving on 127.0.0.1:8080")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
