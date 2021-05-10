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


