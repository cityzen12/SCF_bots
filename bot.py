import requests
import json
import schedule
import time

def push():
    webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=176caa06-3d2d-4b16-8657-9084f90d32ac'
    headers = {'content-type': 'application/json'}
    data =  {
    "msgtype": "markdown",
    "markdown": {
        "content": "**今天吃什么**",
        "attachments": [{
            "callback_id": "button_two_row",
            "actions": [{
                    "name": "button_1",
                    "text": "3楼",
                    "type": "button",
                    "value": "D2-3F",
                    "replace_text": "你已选择D2-3F",
                    "border_color": "9AC8E2",
                    "text_color": "9AC8E2"
                },
                {
                    "name": "button_2",
                    "text": "4楼",
                    "type": "button",
                    "value": "D2-4F",
                    "replace_text": "你已选择D2-4F",
                    "border_color": "DB7D74",
                    "text_color": "DB7D74"
                },
                {
                    "name": "button_3",
                    "text": "2楼",
                    "type": "button",
                    "value": "D2-2F",
                    "replace_text": "你已选择D2-2F",
                    "border_color": "E799B0",
                    "text_color": "E799B0"
                },
                {
                    "name": "button_4",
                    "text": "火锅！",
                    "type": "button",
                    "value": "hotpot",
                    "replace_text": "你已选择火锅！",
                    "border_color": "576690",
                    "text_color": "576690"
                },
            ]
        }
        ]
    }
}
    p = requests.post(webhook, headers = headers, data = json.dumps(data))
    p.encoding = 'utf-8'
    return(p.text)  


schedule.every().day.at("17:30").do(push)

while True:
    schedule.run_pending()
    print('monitoring...')
    time.sleep(10)