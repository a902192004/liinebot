import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, FollowEvent, JoinEvent,
    TextSendMessage, TemplateSendMessage,
    TextMessage, ButtonsTemplate,
    PostbackTemplateAction, MessageTemplateAction,
    URITemplateAction, ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('n6zOdaPY9y9ZQSwPA5OYHH+J850NP7lHxCnHq++tDsypOcVMSoGWafNbR21Q9o5l9Rva8L5q4L8bIcIZNToIsNWlWWihtUfFjIjlMVFSLg4dHHiFM6zFaTJqizZYUA9H2M+gcg+Qt2NxmvpFo9wf5wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('72ea4287101448a971f8fcb36e873f3f')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID
    elif(text=="你好"):
        reply_text = "親愛的顧客: 你好"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    elif(text=="下注"):
        reply_text = "下注成功"
    else:
        reply_text = text
        
    # switch(text) 
    # {
    #     case "Hi":
    #     reply_text = "Hello";
    #      break;
    #     case "你好":
    #      reply_text = "親愛的顧客: 你好";
    #      break;
    #     case "機器人":
    #      reply_text = "叫我嗎";
    #      break;
    #     case "下注" :
    #      reply_text = "下注成功";
    #      break;
    #     default:
    #      reply_text = text
    # }


    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)    

@app.route('/')
def homepage():
    return 'Hello, World!'


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)