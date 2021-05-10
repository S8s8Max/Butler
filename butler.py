import requests
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

SLACK_BOT_USER_OAUTH_TOKEN = os.environ["SLACK_BOT_USER_OAUTH_TOKEN"]

def SendMessage(text: str):
    client = WebClient(token=SLACK_BOT_USER_OAUTH_TOKEN)
    try:
        response = client.chat_postMessage(channel='#times_sober-wizard', text=text)
    except SlackApiError as e:
        print("Got an Error : ", e)

def ParseMessage(text: str) -> bool:
    length = len(text)
    if length >= 7:
        if text[0] == "[" and text[1] == "/" and text[2] == "m" and text[3] == "e" and text[4] == "m" and text[5] == "o" and text[6] == "]":
            return True

    else:
        return False
