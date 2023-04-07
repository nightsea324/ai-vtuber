import os
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = None
handler = None


def lineInit():
    global line_bot_api, handler
    line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
    handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

    return


def lineHandle(body, signature):
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        err = "Invalid signature. Please check your channel access token/channel secret."
        print(err)
        return err
    return


