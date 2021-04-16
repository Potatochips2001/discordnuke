import requests, json
from time import sleep
import random

auth = {
    "authorization": "Token"
}

emojis = "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫🥱😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😬🤯😩😨😧😦😭😢"
usedEmoji = []

channelId = input("Channel ID: ")

while True:
    ids = input("MSG: ")
    for i in range(20):
        ranE = random.choice(emojis)
        requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{ids}/reactions/{ranE}/@me", headers=auth)
        emojis.replace(ranE, "")
        sleep(0.3)
