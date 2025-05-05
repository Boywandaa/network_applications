from aiohttp import web

async def handle(request):
    return web.json_response({"message": "Hello from aiohttp server!"})

app = web.Application()
app.add_routes([web.get('/', handle)])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
