import requests


def main():
    response = requests.get("https://www.google.com")

    print(response.text)

main()