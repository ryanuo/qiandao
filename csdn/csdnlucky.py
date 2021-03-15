import requests
import os
if __name__ == '__main__':
    USERNAME = os.environ["USERNAME"]  # 这里是’CSDN‘的用户名，链接后面的
    LUCKYCOOKIE = os.environ["LUCKYCOOKIE"]  # 点击签到后在控制台从heard里面找到COOKIE

# 第一步获取请求数据
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-length': '246',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': LUCKYCOOKIE,
    'origin': 'https://i.csdn.net',
    'pragma': 'no-cache',
    'referer': 'https://i.csdn.net/',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    }
data = {
    'ip': "",
    'platform': "pc-my",
    'product': "pc",
    'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    'username': USERNAME,
    'uuid': "10_10212595300-1608558661367-119405"
}
# 第二步 post请求

getpost = requests.post("https://me.csdn.net/api/LuckyDraw_v2/goodLuck",headers=headers,data=data).content.decode("unicode_escape")
# 输出请求结果
print(getpost)
# print(type(getpost))  # 输出字符串形式
import json
# 将已编码的 JSON 字符串解码为 Python 对象 字典
# print(type(json.loads(getpost)))  # 返回形式字典
option = json.loads(getpost)['data']['msg']
# 获取抽奖详情
print(option)
