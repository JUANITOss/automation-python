import requests, webbrowser

res = requests.get(r'https://chatgpt.com/')

htmlFromWeb = open(r"htmlFromWeb.txt", "wb")

for chunk in res.iter_content(1000000):
    htmlFromWeb.write(chunk)