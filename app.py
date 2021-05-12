# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import requests
import json

DEBUG = False
if DEBUG:
    from butler_local import SendMessage, ParseMessage
else:
    from butler import SendMessage, ParseMessage


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
        print("get event")
        event = data['event']
        if 'user' in event:
            print("user = ", event["user"])
        if "text" in event:
            print("text = ", event["text"])
            text_data = event["text"]

    if ParseMessage(text_data):
        SendMessage("Successed!")
        # ここで自然言語処理



    return Response("nothing", mimetype='text/plane')


if __name__ == '__main__':
    app.run()

