# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import requests
import json

# Self-dev
from NLP import NLP
from Search import Search

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

    # for challenge of slack api
    if 'challenge' in data:
        token = str(data['challenge'])
        return Response(token, mimetype='text/plane')
    # for events which you added
    if 'event' in data:
        event = data['event']
        if 'user' in event:
            print("user = ", event["user"])
        if "text" in event:
            print("text = ", event["text"])
            text_data = event["text"]

    message = ""

    if CheckMessage(text_data):
        # NLP here.
        result = NLP(text_data)
        # Search academic papers from arxive.
        papers = Search(result)

        # Make a message including info about papers.
        if isinstance(result, list):
            for i in range(len(result)):
                message += f"{i+1} : {result[i]}\n"
        SendMessage(message)

    return Response(message, mimetype='text/plane')


if __name__ == '__main__':
    app.run()

