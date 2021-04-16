import requests
import time
import json

auth = {
    "authorization": "Token to be used"
}

ids = []
n = int(0)

channelId = input("Channel ID: ")

while True:
    getLastMessage = requests.get(f"https://discord.com/api/v8/channels/{channelId}/messages?limit=1", headers=auth)
    lastPacket = json.loads(getLastMessage.text)
    lastMsg = lastPacket[0]['content']
    lastId = lastPacket[0]['id']
    if ("lmao" in lastMsg.lower() or "lmfao" in lastMsg.lower() or "ass" in lastMsg.lower()) and lastId not in ids:
        ids.append(lastId)
        requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{lastId}/reactions/🍑/@me", headers=auth)
        n += 1;print(f"emojis used: {n}", end='\r')
    if "euphoria" in lastMsg.lower() and lastId not in ids:
        ids.append(lastId)
        requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{lastId}/reactions/💊/@me", headers=auth)
        n += 1;print(f"emojis used: {n}", end='\r')
    if "example" in lastMsg.lower() and lastId not in ds:
        ids.append(lastId)
        #for custom emojis you have to put emojiname:emojiID; You can find emoji ID by putting backslash emoji in chat and it will show you in chat.
        requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{lastId}/reactions/{emojiname:666}/@me", headers=auth)
    time.sleep(0.3)
