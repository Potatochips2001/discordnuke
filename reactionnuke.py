import requests, json
from time import sleep

auth = {
    "authorization": "Token"
}

channelId = input("Channel ID: ")
reactionsToUse = int(input("Count: "))

packet = requests.get(f"https://discord.com/api/v8/channels/{channelId}/messages?limit={reactionsToUse}", headers=auth)
packetJson = json.loads(packet.text)

for i in range(reactionsToUse):
    requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{str(packetJson[i]['id'])}/reactions/📠/@me", headers=auth)
    sleep(0.2)
