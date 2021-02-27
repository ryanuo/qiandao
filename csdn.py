import requests
import os  #加入环境变量
if __name__ == '__main__':
    COOKIE = os.environ["COOKIE"]
    USERNAME = os.environ["USERNAME"]
    DDSECRET = os.environ["DDSECRET"]  # 钉钉通知加签
    DDPOSTURL = os.environ["DDPOSTURL"]  # 钉钉通知机器人的链接地址

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '246',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': COOKIE,
    'origin': 'https://i.csdn.net',
    'referer': 'https://i.csdn.net/',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

data = {
    'ip': '',
    'platform': 'pc-my',
    'product': 'pc',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'username': USERNAME,
    'uuid': '10_10212595300-1608558661367-119405',
}

r = requests.post("https://me.csdn.net/api/LuckyDraw_v2/signIn",headers=headers,data=data).content.decode("unicode_escape")
print(r)
import json
timedata = json.loads(r)
# 将json转化为数组形式
print(timedata)
isSign = timedata['data']['isSigned']
# print(isSign) #返回签到是否成功
t = timedata['data']['msg']


# 通知模块
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests, json

timestamp = str(round(time.time() * 1000))
secret = DDSECRET
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
# 导入依赖库
headers = {'Content-Type': 'application/json'}  # 定义数据类型
# 截至到&timestamp之前
webhook = DDPOSTURL + timestamp + "&sign=" + sign
# 定义要发送的数据
# "at": {"atMobiles": "['"+ mobile + "']"
if isSign:
    data = {
    #定义内容
    "msgtype": "markdown",
     "markdown": {
         "title":"CSDN签到通知",
         "text": ">CSDN 签到已成功\n - 签到详情:" + "\n"+ t
     }
      }
    res = requests.post(webhook, data=json.dumps(data), headers=headers)   #发送post请求
    print(res.text)
else:
    data = {
        # 定义内容
        "msgtype": "markdown",
        "markdown": {
            "title": "CSDN签到通知",
            "text": "签到失败" + t
        }
    }
    res = requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
    print(res.text)
