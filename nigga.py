import requests
from time import sleep

auth = {
    "authorization": "token"
}

channel = input("Channel ID: ")

def post(msgid):
    requests.put(f"https://discord.com/api/v8/channels/{channel}/messages/{msgid}/reactions/🇳/@me", headers=auth)
    sleep(0.1)
    requests.put(f"https://discord.com/api/v8/channels/{channel}/messages/{msgid}/reactions/🇮/@me", headers=auth)
    sleep(0.1)
    requests.put(f"https://discord.com/api/v8/channels/{channel}/messages/{msgid}/reactions/🇬/@me", headers=auth)
    sleep(0.1)
    requests.put(f"https://discord.com/api/v8/channels/{channel}/messages/{msgid}/reactions/🇪/@me", headers=auth)
    sleep(0.1)
    requests.put(f"https://discord.com/api/v8/channels/{channel}/messages/{msgid}/reactions/🇷/@me", headers=auth)

while True:
    global msg
    msg = input("Message ID: ")
    post(msg)
