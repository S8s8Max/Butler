# -*- coding: utf-8 -*-

import requests
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

SLACK_BOT_USER_OAUTH_TOKEN = os.environ["SLACK_BOT_USER_OAUTH_TOKEN"]

def SendMessage(text: str):
    """
    引数のテキストをターゲットのチャンネルに投稿する関数。
    """
    client = WebClient(token=SLACK_BOT_USER_OAUTH_TOKEN)
    try:
        response = client.chat_postMessage(
            channel='#times_sober-wizard',
            text=text
        )
    except SlackApiError as e:
        print("Got an Error : ", e)


def CheckMessage(text: str) -> bool:
    """
    テキストが文頭に　[/memo] という文字列を含む時にだけNLPする
    """
    key_str = "[/memo]"
    length = len(text)

    if key_str in text:
        return True
    else:
        return False
