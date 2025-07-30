import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = "UC_fsItngqg0EFbMCZtFgUjg"

def get_subscriber_count():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    subs = data["items"][0]["statistics"]["subscriberCount"]
    return subs

print("Tracking Live Youtube Subscribers..... \n")
while True:
    subs = get_subscriber_count()
    print(f"Subscriber: {subs}")
    time.sleep(5)