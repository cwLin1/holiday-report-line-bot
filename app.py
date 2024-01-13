from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from datetime import datetime, timedelta

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ghzL1xG7qr/QX7Qt32hBTUrIFLB4paY02TxoDUiFFojkdyohBzO5oe7gr6wflY2AyNLXv3Lt60ZCgCm9gERcLqAREnkfsi+2Kgcjf/Xgc+D5CMLGtdki/b2lrxyM9eQ4wSLf++QN9+PW7Y0rUBjmswdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('66dbe404b72cfffd46a00a37074b82d3')

reports = { '050 林正偉': '未回報', 
            '051 黃彥維': '未回報', 
            '052 高詠峻': '未回報', 
            '053 楊義庠': '未回報', 
            '054 吳炫霖': '未回報', 
            '055 陳柏岳': '未回報', 
            '056 陳建樺': '未回報', 
            '057 許佑澤': '未回報', 
            '058 華紹甯': '未回報', 
            '059 黃睦懿': '未回報', 
            '060 許智勛': '未回報', 
            '061 翁健庭': '未回報', 
            }
reports = {}


def timestamp_to_time(timestamp):

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp) + timedelta(hours = 8)
    return f'{dt_object.hour:02d}' + f'{dt_object.minute:02d}'

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
    global reports
    text = event.message.text

    if text == '回報':
        report_text = ''
        report_list = []
        for k in reports:
            report_list.append(k + ' ' + reports[k]['time'] + ' ' + reports[k]['state'])
        report_text = '\n'.join(report_list)
        message = TextSendMessage(text=report_text)
        line_bot_api.reply_message(event.reply_token, message)

    # elif text == '返營回報':
    #     # report_text = ''
    #     report_list = []
    #     for k in reports:
    #         report_list.append(k + ' ' + reports[k]['state'])
    #     report_text = '\n'.join(report_list)

    #     message = TextSendMessage(text=report_text)
    #     line_bot_api.reply_message(event.reply_token, message)

    elif text[:2] == '設定':
        users = text.split('\n')
        reports = {}
        for user in users[1:]:
            reports[user] = {'time':'', 'state':'未回報'}
        message = TextSendMessage(text='已更新成員!')
        line_bot_api.reply_message(event.reply_token, message)

    elif text[:2] == '重置':
        users = text.split('\n')
        for user in reports:
            reports[user] = {'time':'', 'state':'未回報'}
        message = TextSendMessage(text='已重置回報!')
        line_bot_api.reply_message(event.reply_token, message)

    else:
        rep = text.split(' ')
        if len(rep) >= 2:
            key = rep[0] + ' ' + rep[1]
            if key in reports:
                timestamp = event.timestamp // 1000
                curr_time = timestamp_to_time(timestamp)
                state = ' ' .join(rep[2:])
                reports[key]['time'] = curr_time
                reports[key]['state'] = state
                # reports[key] = state
                message = TextSendMessage(text='已更新回報狀態!')
                line_bot_api.reply_message(event.reply_token, message)

    


    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
