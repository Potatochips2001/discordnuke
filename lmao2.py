import requests, json
from time import sleep
import random

auth = {
    "authorization": "Token"
}

emojis = "๐๐๐๐คฃ๐๐๐๐๐๐๐๐๐๐๐ฅฐ๐๐๐โบ๐๐ค๐คฉ๐ค๐คจ๐๐๐ถ๐๐๐ฃ๐ฅ๐ฎ๐ค๐ฏ๐ช๐ซ๐ฅฑ๐ด๐๐๐๐๐คค๐๐๐๐๐๐ค๐ฒโน๐๐๐๐๐ค๐ฌ๐คฏ๐ฉ๐จ๐ง๐ฆ๐ญ๐ข"
usedEmoji = []

channelId = input("Channel ID: ")

while True:
    ids = input("MSG: ")
    for i in range(20):
        ranE = random.choice(emojis)
        requests.put(f"https://discord.com/api/v8/channels/{channelId}/messages/{ids}/reactions/{ranE}/@me", headers=auth)
        emojis.replace(ranE, "")
        sleep(0.3)
