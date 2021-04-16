import requests
import json
import time

auth = {
    "authorization": "" #your discord token
}

channelId = "" #replace with your channel id

ids = []

while True:
    packet = requests.get(f"https://discord.com/api/v8/channels/{channelId}/messages?limit=1", headers=auth)
    msgId = json.loads(packet.text)[0]['id']
    if msgId not in ids:
        packet = requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{msgId}/reactions/🤪/@me", headers=auth)
        print(packet)
        ids.append(msgId)
    time.sleep(0.2) #you can put whatever time you want here
