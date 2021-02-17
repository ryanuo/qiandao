import requests
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '246',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'uuid_tt_dd=10_10212595300-1608558661367-119405; UN=www1577791638; p_uid=U010000; UserName=www1577791638; UserInfo=d4dff64ebf604c1db4135d32df9a2b12; UserToken=d4dff64ebf604c1db4135d32df9a2b12; UserNick=Harry-iu; AU=FFA; BT=1613455397205; ssxmod_itna=QqAxBDcDy7iQTqmq0dbk9D9lYYeO700DiIouKD/8iIDnqD=GFDK40EogqD7tyorjuG+Wx5Gx2GQEQmh0fmdaDocG1ESO40aDbqGkqQO74GGjxBYDQxAYDGDDPDogPD1D3qDkXxYPGW8qiaDGeDec9ODY5DhxDC00PDwx0C6rYHY85mn=Dh=nikD7vmDlP4wUTkQbfEMnH3vx0k040OBOHkuxoDUCRTmi0eO=9DEibq3lTewYeK3mreYv24I7CT=i4oiyuPk5QDi2=K4D; ssxmod_itna2=QqAxBDcDy7iQTqmq0dbk9D9lYYeO700DiIobG9ikDGEheGX9qGaK7EksrxKwPK08DewpD===; c_segment=13; dc_sid=fd413ade0fb4a99557ffd7cc35ad4225; c_first_ref=www.google.com; aliyun_webUmidToken=T2gAPNhLEOcT4VGBuT3EC5gHkqw0Hetk0I0x0c4Q45GNUM30Ed7KJPMOIMKb9UR6AZQ=; dc_session_id=10_1613545224614.710431; c_first_page=https%3A//blog.csdn.net/weixin_45635130/article/details/107911178; announcement-new=%7B%22isLogin%22%3Atrue%2C%22announcementUrl%22%3A%22https%3A%2F%2Fblog.csdn.net%2Fblogdevteam%2Farticle%2Fdetails%2F112280974%3Futm_source%3Dgonggao_0107%22%2C%22announcementCount%22%3A0%2C%22announcementExpire%22%3A3600000%7D; c_pref=https%3A//blog.csdn.net/aian1614/article/details/102293438%3Futm_medium%3Ddistribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.control%26depth_1-utm_source%3Ddistribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.control; c_ref=https%3A//blog.csdn.net/ydydyd00/article/details/80882183; c_utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-7; c_page_id=default; dc_tos=qonwpu; log_Id_pv=870; log_Id_view=1162; log_Id_click=486',
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
    'username': 'www1577791638',
    'uuid': '10_10212595300-1608558661367-119405',
}

r = requests.post("https://me.csdn.net/api/LuckyDraw_v2/signIn",headers=headers,data=data).content.decode("unicode_escape")
print(r)