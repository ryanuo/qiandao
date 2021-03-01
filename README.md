## 仓库简介

1. Python+GitHub实现CSDN的自动签到，并用钉钉机器人通知
2. 满足抽奖条件执行抽奖操作
3. 网易云音乐签到

## 仓库文件介绍

1. csdn.py 没有抽奖的操作，只有签到
2. csdn1.py 包括抽奖和签到
3. csdnlucky.py 是只有抽奖的操作
4. wyy.py 网页端网易云签到

## 签到内容

1. csdn 签到得积分
2. 暂定一个
![效果图](https://cdn.jsdelivr.net/gh/Rr210/image@master/hexo/4/csdn39173172.webp)
## 使用方法

1. 将以上代码中`headers`和`data`替换成你自己的
2. 点击这里【[签到地址](https://i.csdn.net/#/user-center/draw)】,打开浏览器调式工具`console`，`F12`或者`ctrl+shift+i`,点击`network`后点击签到控制台会生成新的文件，点击后获得此时的`header`和`data`，`ctrl+c`复制下来
3. 转换成字典形式，转换方法【[查看方法](https://blog.csdn.net/weixin_44146025/article/details/113249043?spm=1001.2014.3001.5501)】，当然嫌麻烦可以手动修改成字典形式

## Github配置

1. 将你的COOKIE和USERNAME 保存替换成以上样式，记得保存好COOKIE，将COOKIE使用环境变量放到GitHub仓库的secrets里面，如图所示
2. 修改代码第15行，第31行，第56行，第65行  将自己的信息修改
![](https://cdn.jsdelivr.net/gh/Rr210/image@master/hexo/4/csdnpyrr.webp)
2. 各个参数介绍

|  Secrets  |                           参数介绍                           |
| :-------: | :----------------------------------------------------------: |
|  COOKIE   |       这个时签到csdn所需的COOKIE，识别用户身份必须获得       |
| USERNAME  |                       你的CSDN的用户名                       |
| DDPOSTURL | 钉钉群机器人的webhook地址，参考钉钉[官方文档](https://developers.dingtalk.com/document/app/custom-robot-access) |
| DDSECRET  |                  设置钉钉机器人时的加签密钥                  |
| LUCKYCOOLKIE| 执行抽奖时所需的COOKIR，获取方法与签到的cookie相同|
| WYYCOOKIE| 获取方法相同|
| WYYCSRFTOKEN| 在控制台获取 csrf_token 的值|

## 设置定时

1. 将`.github`文件下的`workflows`中的`csdn.yml`中的`corn`的属性值修改
2. 注意时差`mg`比我们地区快8个小时


## 参考

- 【[参考的文章](https://www.cnblogs.com/Neeo/articles/11511087.html)】