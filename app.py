# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import requests
import json

# Self-dev
from NLP import NLP
from Search import SearchArxiv

DEBUG = False

if DEBUG:
    from butler_local import SendMessage, CheckMessage
else:
    from butler import SendMessage, CheckMessage


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'


# Slackからデータがポストされた時の挙動
@app.route("/api", methods=["POST"])
def post():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    text_data = ""

    # for challenge of slack api
    if 'challenge' in data:
        token = str(data['challenge'])
        return Response(token, mimetype='text/plane')
    # for events which you added
    if 'event' in data:
        event = data['event']
        if "text" in event:
            print("Got text : ", event["text"][0:10]+"...")
            text_data = event["text"]

    message = ""

    if len(text_data) > 1 and CheckMessage(text_data):
        # NLP here.
        result = NLP(text_data)
        # Search academic papers from arxive.
        papers_info = SearchArxiv(result)
        message += papers_info
        SendMessage(message)

    return Response(message, mimetype='text/plane')


if __name__ == '__main__':
    app.run()


# curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/ -d '{"event":{"text":"機械学習　フェイク"}}'
