import requests
import os
if __name__ == '__main__':
    WYYCOOKIE = os.environ["WYYCOOKIE"]  # 点击签到后在控制台从heard里面找到COOKIE
    WYYCSRFTOKEN = os.environ["WYYCSRFTOKEN"]
    DDSECRET = os.environ["DDSECRET"]  # 钉钉通知加签
    DDPOSTURL = os.environ["DDPOSTURL"]
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-length': '410',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': WYYCOOKIE,
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/discover',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
}
csrf_token = WYYCSRFTOKEN
data = {
    'params': 'CBp2MeAmSpBLtknx4gc4XJtqeLT8a5CqE8026TJu/GN4csIzX3/mz1oCscm1wqrUeh3oq5tGYK1FGWKm2Hxz0grQu4mJArXnFNILjOrlV+k3PLli+FNMpOHYQojhTzt5',
    'encSecKey': '793b1667327277870b34d8fde27454e67364d3cd2b0deb1302089f3dcebf759c9e411d0cf28aa8b1351818c56d7c85a7685079dfcf17ec741088064c6baa2a5e416090132aea4b23f5eaecbf1dcf8b35dc087b7439d754dc3ecff98b0c1a1f9647c3221452e3d95adc1a77273390bee4146a9cdfea292b9c21cf5fab19676855'
}
wyy_data = requests.post("https://music.163.com/weapi/point/dailyTask?csrf_token="+csrf_token,headers=headers,data=data)
import json
print(json.loads(wyy_data.text))
# 获取签到详情
wyycode = json.loads(wyy_data.text)['code']
# response = json.loads(wyy_data.text)['msg']

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
if wyycode == 200:
    data = {
    # 定义内容
    "msgtype": "markdown",
     "markdown": {
         "title": "网易云签到通知",
         "text": ">网易云签到 签到已成功\n - 签到详情: 签到成功"
     }
      }
    res = requests.post(webhook, data=json.dumps(data), headers=headers)   #发送post请求
    print(res.text)
else:
    data = {
        # 定义内容
        "msgtype": "markdown",
        "markdown": {
            "title": "网易云签到通知",
            "text": "签到失败 \n- 签到详情: 签到成功"
        }
    }
    res = requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
    print(res.text)
