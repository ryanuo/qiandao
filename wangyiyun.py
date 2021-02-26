import os
import re
from DecryptLogin import login
from DecryptLogin.platforms.music163 import Cracker

'''网易云音乐自动签到'''
class NeteaseSignin():
    def __init__(self, username, password, **kwargs):
        self.username = username
        self.session = NeteaseSignin.login(username, password)
        self.csrf = re.findall('__csrf=(.*?) for', str(self.session.cookies))[0]
        self.cracker = Cracker()
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Referer': 'http://music.163.com/discover',
                        'Accept': '*/*'
                    }
    '''外部调用'''
    def run(self):
        # 签到接口
        signin_url = 'https://music.163.com/weapi/point/dailyTask?csrf_token=' + self.csrf
        # 模拟签到(typeid为0代表APP上签到, 为1代表在网页上签到)
        typeids = [0, 1]
        for typeid in typeids:
            client_name = 'Web端' if typeid == 1 else 'APP端'
            # --构造请求获得响应
            data = {
                        'type': typeid
                    }
            data = self.cracker.get(data)
            res = self.session.post(signin_url, headers=self.headers, data=data)
            res_json = res.json()
            # --判断签到是否成功
            if res_json['code'] == 200:
                print('[INFO]: 账号%s在%s签到成功...' % (self.username, client_name))
            else:
                print('[INFO]: 账号%s在%s签到失败, 原因: %s...' % (self.username, client_name, res_json.get('msg')))
    '''模拟登录'''
    @staticmethod
    def login(username, password):
        lg = login.Login()
        _, session = lg.music163(username, password)
        return session

'''run'''
if __name__ == '__main__':
    username = os.environ["NETEASE_USERNAME"]
    password = os.environ["NETEASE_PASSWORD"]
    sign_in = NeteaseSignin(username=username, password=password)
    sign_in.run()
