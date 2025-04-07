import asyncio

def main():

    async def say_hello():
        print("hello_world")
        await(5)

    async def say_goodbye():
        print("goodbye")

if __name__ == "__main__":
    main()