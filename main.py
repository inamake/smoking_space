# -*- coding: utf-8 -*-

from flask import Flask, request, abort

from collections import defaultdict

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage,
)
import os

app = Flask(__name__)

#空の辞書を宣言
addressData = defaultdict(dict)

#分岐スイッチ
sw0 = False


#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#おうむ返しする。
#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
#    line_bot_api.reply_message(
#        event.reply_token,
#        TextSendMessage(text=event.message.text))

#アプリ起動を行う。
@handler.add(MessageEvent, message=TextMessage)
def start(event):
    global sw0
    if event.message.text == "喫煙所" and sw0 == False:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="登録を行います。\n『位置情報』を送ってください。")
        )
        sw0 = True

    elif sw0 == False:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="『喫煙所』と入力してアプリを起動してください。")
        )

@handler.add(MessageEvent, message=LocationMessage)


#位置情報から住所、緯度、経度を返す。
#def return_address(event):
#    line_bot_api.reply_message(
#        event.reply_token,
#        [
#            TextSendMessage(text="住所:\n[{}]\n緯度:\n[{}]\n経度:\n[{}]".format(event.message.address,
#            event.message.latitude,event.message.longitude)),
#        ]
#    )

#位置情報から郵便番号と郵便番号上3桁と住所を返す。
def return_postal_code(event):
    global addressData
    global sw0
    if sw0 == True and event.message.type == 'location':
        Address = event.message.address
        Postal_code_frist3 = Address[4:7]
        addressData[Postal_code_frist3]["Address"] = Address
        #postal_code = postal_code_frist3 + address[8:12]
        line_bot_api.reply_message(
            event.reply_token,
            [
                #TextSendMessage(text="郵便番号上3桁:\n[{}]\n住所:\n[{}]".format(Postal_code_frist3,Address)),
                TextSendMessage(text=addressData[Postal_code_frist3]["Address"])
            ]
        )
        sw0 = False



    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="『位置情報』を送ってください。")
        )
        sw0 = False

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
