import requests,base64,json,hashlib,os
if __name__ == '__main__':
    DDSECRET = os.environ["DDSECRET"]  # 钉钉通知加签
    DDPOSTURL = os.environ["DDPOSTURL"]  # 钉钉通知机器人的链接地址
from Crypto.Cipher import AES
def encrypt(key, text):
    cryptor = AES.new(key.encode('utf8'), AES.MODE_CBC, b'0102030405060708')
    length = 16                    
    count = len(text.encode('utf-8'))     
    if (count % length != 0):
        add = length - (count % length)
    else:
        add = 16             
    pad = chr(add)
    text1 = text + (pad * add)    
    ciphertext = cryptor.encrypt(text1.encode('utf8'))          
    cryptedStr = str(base64.b64encode(ciphertext),encoding='utf-8')
    return cryptedStr
def md5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()
def protect(text):
    return {"params":encrypt('TA3YiYCfY2dDJQgg',encrypt('0CoJUm6Qyw8W8jud',text)),"encSecKey":"84ca47bca10bad09a6b04c5c927ef077d9b9f1e37098aa3eac6ea70eb59df0aa28b691b7e75e4f1f9831754919ea784c8f74fbfadf2898b0be17849fd656060162857830e241aba44991601f137624094c114ea8d17bce815b0cd4e5b8e2fbaba978c6d1d14dc3d1faf852bdd28818031ccdaaa13a6018e1024e2aae98844210"}


s=requests.Session()
header={}
url="https://music.163.com/weapi/login/cellphone"
url2="https://music.163.com/weapi/point/dailyTask"
url3="https://music.163.com/weapi/v1/discovery/recommend/resource"
logindata={
    "phone":input(),
    "countrycode":"86",
    "password":md5(input()),
    "rememberLogin":"true",
}
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        "Referer" : "http://music.163.com/",
        "Accept-Encoding" : "gzip, deflate",
        }
headers2 = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        "Referer" : "http://music.163.com/",
        "Accept-Encoding" : "gzip, deflate",
        "Cookie":"os=pc; osver=Microsoft-Windows-10-Professional-build-10586-64bit; appver=2.0.3.131777; channel=netease; __remember_me=true;"
        }

res=s.post(url=url,data=protect(json.dumps(logindata)),headers=headers2)
tempcookie=res.cookies
object=json.loads(res.text)


# 钉钉通知模块
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

if object['code']==200:
    print("登录成功！")
else:
    print("登录失败！请检查密码是否正确！"+str(object['code']))
    exit(object['code'])

res=s.post(url=url2,data=protect('{"type":0}'),headers=headers)
object=json.loads(res.text)
if object['code']!=200 and object['code']!=-2:
    print("签到时发生错误："+object['msg'])
else:
    if object['code'] == 200:
        print("签到成功，经验+"+str(object['point']))

    else:
        data = {
            # 定义内容
            "msgtype": "markdown",
            "markdown": {
                "title": "网易云2签到信息通知",
                "text": ">您已重复签到,请不要重复操作\n"
            }
        }
        res1 = requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
        print(res1.text)
        print("重复签到")


res=s.post(url=url3,data=protect('{"csrf_token":"'+requests.utils.dict_from_cookiejar(tempcookie)['__csrf']+'"}'),headers=headers)
object=json.loads(res.text,strict=False)
for x in object['recommend']:
    url='https://music.163.com/weapi/v3/playlist/detail?csrf_token='+requests.utils.dict_from_cookiejar(tempcookie)['__csrf']
    data={
        'id':x['id'],
        'n':1000,
        'csrf_token':requests.utils.dict_from_cookiejar(tempcookie)['__csrf'],
    }
    res=s.post(url,protect(json.dumps(data)),headers=headers)
    object=json.loads(res.text,strict=False)
    buffer=[]
    count=0
    for j in object['playlist']['trackIds']:
        data2={}
        data2["action"]="play"
        data2["json"]={}
        data2["json"]["download"]=0
        data2["json"]["end"]="playend"
        data2["json"]["id"]=j["id"]
        data2["json"]["sourceId"]=""
        data2["json"]["time"]="240"
        data2["json"]["type"]="song"
        data2["json"]["wifi"]=0
        buffer.append(data2)
        count+=1
        if count>=310:
            break
    if count>=310:
        break
url = "http://music.163.com/weapi/feedback/weblog"
postdata={
    "logs":json.dumps(buffer)
}
res=s.post(url,protect(json.dumps(postdata)))
object=json.loads(res.text,strict=False)
if object['code']==200:
    data = {
        # 定义内容
        "msgtype": "markdown",
        "markdown": {
            "title": "网易云2签到信息通知",
            "text": ">您已签到成功\n - 签到详情:\n" + object['msg'] + "\n" + "\n签到成功，经验+" + str(
                object['point']) + "\n" + "\n刷单成功！共" + str(count) + "首"
        }
    }
    res1 = requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
    print(res1.text)
    print("刷单成功！共"+str(count)+"首")
    exit()
else:
    print("发生错误："+str(object['code'])+object['message'])
    exit(object['code'])