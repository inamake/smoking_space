from flask import Flask, request, abort

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=LocationMessage)
# 位置情報から住所、緯度、経度を返す。
def return_address(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="住所:\n[{}]\n緯度:\n[{}]\n経度:\n[{}]".format(event.message.address,
            event.message.latitude,event.message.longitude)),
        ]
    )


#位置情報から郵便番号と郵便番号上3桁を返す。
def return_postal_code(event):
    address = event.message.address
    postal_code_frist3 = address[5:7]
    postal_code = postal_code_frist3 + address[9:12]
    line_bot_api.reply_message(
        event.reply_token,
        [
        TextSendMessage(text="郵便番号:[{}]\n郵便番号上3桁:[{}]\n".format(postal_code,postal_code_frist3)),
        ]
    )

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
