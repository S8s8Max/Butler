from slack_api_token import SLACK_BOT_USER_OAUTH_TOKEN, SLACK_USER_OAUTH_TOKEN
import requests
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def SendMessage(text: str):
    client = WebClient(token=SLACK_BOT_USER_OAUTH_TOKEN)
    try:
        response = client.chat_postMessage(channel='#times_sober-wizard', text=text)
    except SlackApiError as e:
        print("Got an Error : ", e)

if __name__ == "__main__":
    text = sys.argv[1]

    SendMessage(text)
