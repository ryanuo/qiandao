import requests, json, time, hmac, hashlib, base64, urllib.parse, os, requests, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
Csdn签到和抽奖
'''


class Csdn:
    def __init__(self):
        self.headers = {
            'content-type': 'application/json;charset=UTF-8',
            'cookie': "",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4483.0 Safari/537.36'
        }
        self.data = {
            "ip": "",
            "platform": "pc-my",
            "product": "pc",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4483.0 Safari/537.36",
            "username": USERNAME,
            "uuid": ""
        }

    def draws(self):
        self.headers[
            'cookie'] = COOKIE_DRAW
        self.data['uuid'] = '10_19718702780-1615518137009-545439'
        res = requests.post('https://me.csdn.net/api/LuckyDraw_v2/goodLuck', headers=self.headers, data=self.data)
        data_draw = json.loads(res.text)
        if data_draw['code'] == 200:
            return data_draw['data']
        else:
            return '抽奖失败'

    def signed(self):
        self.headers[
            'cookie'] = COOKIE_SIGNED
        self.data['uuid'] = '10_10213081380-1623757365901-112902'
        res = requests.post('https://me.csdn.net/api/LuckyDraw_v2/signIn', headers=self.headers, data=self.data)
        return json.loads(res.text)

    def notice(self):
        # 钉钉通知模块
        timestamp = str(round(time.time() * 1000))
        secret = DD_SECRET
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        # 导入依赖库
        headers = {'Content-Type': 'application/json'}  # 定义数据类型
        # 截至到&timestamp之前
        webhook = DD_POSTURL + timestamp + "&sign=" + sign
        data = {
            # 定义内容
            "msgtype": "markdown",
            "markdown": {
                "title": "CSDN抽奖通知",
                "text": "csdn抽奖>\n - 抽奖详情:\n" + t + "\n" + '\n- 签到详情' + r
            }
        }
        res = requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
        # print(res.text)

    def QQ_notice(self):
        msg_from = QQ_SEND.split('+')[0]  # 发送方邮箱
        passwd = QQ_SEND.split('+')[1]  # 就是上面的授权码
        to = [QQ_ACCEPT]  # 接受方邮箱
        msg = MIMEMultipart()  # 设置邮件内容 # MIMEMultipart类可以放任何内容
        text = r + t
        content = '''<head><style>::-webkit-scrollbar {width: 6px;height: 5px;}::-webkit-scrollbar-track {background-color: rgba(50, 57, 61, 0.2);border-radius: 2em;}::-webkit-scrollbar-thumb {background-color: #202b33;background-image: -webkit-linear-gradient(45deg, hsla(0, 0%, 100%, 0.4) 25%, transparent 0, transparent 50%, hsla(0, 0%, 100%, .4) 0, hsla(0, 0%, 100%, .4) 75%, transparent 0, transparent);border-radius: 2em;}</style></head><body><div class="email" style="width: 340px; height: 400px; background-color: #cce2dd; margin-top: 50px; margin-left: auto; margin-right: auto;border-radius: 16px; box-shadow: 1px 2px 5px rgb(0,0,0,0.3);position: relative; overflow: hidden;"><img src="https://cdn.jsdelivr.net/gh/Rr210/image@master/hexo/4/0072Vf1pgy1foxlhi4bpsj31kw0w0qs8.jpg" alt="" style="display: block; width: 100%;"><h3 style="background:hsla(249, 13%, 20%, 0.659); border-radius: 10px;width: 80%;height: 40px; line-height: 40px; text-align: center;font-size: 16px; position: absolute;top: 88px;left: 34px;color: #e7dfee;"> 别慌别慌~~这只是一条提醒!!</h3><h4 style="position:absolute;top: 45px;right:12px;height: 30px; color: #1f3834;">————来自【iui9】的提醒:</h4><div readonly="readonly" style="margin:20px auto 0; display: flex; justify-content: center; align-items: center; border-radius:10px; outline:none; padding: 10px; background-color: hsla(220, 12%, 65%, 0.478);resize:none;max-width: 300px;height: 100px;max-height: 100px; box-shadow: 0 0 10px #352c2c3b;border: 1px solid #a0b3d6; font-size: 12px; overflow-wrap: break-word;-webkit-user-modify: read-only">''' + text + '''</div><div style="font-size: 12px;margin:20px 0 0;display: flex; justify-content: center; align-items: center; text-align: center;color:#200f0f;"> <div>©2021 by</div><a style="text-decoration:none; color:#7c4a0d; margin-left: 5px;" href="https://u.mr90.top">Harry</a></div><h6 style="color: #901594;right:10px;bottom:-20px;position: absolute;">by <a href="https://github.com/Rr210/" target="_blank">Harry</a></h6></div></body>
        '''
        msg.attach(MIMEText(content, 'html', 'utf-8'))  # 把内容加进去
        # msg.attach(MIMEText(conntent, 'plain', 'utf-8'))  # 把内容加进去
        msg['Subject'] = "数据库更新通知"  # 设置邮件主题
        msg['From'] = msg_from  # 发送方信息
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 开始发送  通过SSL方式发送，服务器地址和端口
        s.login(msg_from, passwd)  # 登录邮箱
        s.sendmail(msg_from, to, msg.as_string())  # 开始发送


if __name__ == "__main__":
    COOKIE_DRAW = os.environ["COOKIE_DRAW"]  # 点击签到后在控制台从heard里面找到COOKIE
    COOKIE_SIGNED = os.environ["COOKIE_SIGNED"]  # 点击签到后在控制台从heard里面找到COOKIE
    USERNAME = os.environ["USERNAME"]  # 这里是’CSDN‘的用户名，链接后面的
    DD_SECRET = os.environ["DD_SECRET"]  # 钉钉通知加签
    DD_POSTURL = os.environ["DD_POSTURL"]  # 钉钉通知机器人的链接地址
    QQ_SEND = os.environ['QQ_SEND']  # qq发件人信息格式  邮箱+smtp码 比如：iui9@qq.com+********(加号为分隔符)
    QQ_ACCEPT = os.environ['QQ_ACCEPT']  # qq收件人邮箱地址
    t = str(Csdn().draws())
    r = str(Csdn().signed())
    if len(QQ_ACCEPT) != 0:
        Csdn().QQ_notice()
    if len(DD_SECRET) != 0:
        Csdn().notice()
