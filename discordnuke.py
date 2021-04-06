import requests
import time

chatId = input("Channel ID: ")
msg = input("Message: ")
token = input("Token: ")
delay = float(input("Delay between messages (s): "))

payload = {
     "content": msg
}
head = {
    "authorization": token
}

while True:
    try:
        packet = requests.post(f"https://discord.com/api/v8/channels/{chatId}/messages", data=payload, headers=head)
        if packet.status_code == 200:
            print(f"\rMessages sent: {i}", end='')
        else:
            pass
    except KeyboardInterrupt:
        print("\nScript terminating")
        exit(0)
    except:
        pass
