
name: csdn

on:
  schedule:
    - cron: "0 0 * * *"
  watch:
    types: [started]
jobs:
  build:
    runs-on: ubuntu-latest
    if: github.event.repository.owner.id == github.event.sender.id  # 自己点的 start,测试完记得注释掉
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests lxml
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: 'run py'
      env:
        COOKIE_DRAW: ${{ secrets.COOKIE_DRAW }}  #csdn 请求服务器后返回的，确认身份必备 抽奖
        COOKIE_SIGNED: ${{ secrets.COOKIE_SIGNED }}  #csdn 请求服务器后返回的，确认身份必备 签到
        USERNAME: ${{ secrets.USERNAME }} # 用户名
        DD_SECRET: ${{ secrets.DD_SECRET }} # 钉钉机器人加签密钥
        DD_POSTURL: ${{ secrets.DD_POSTURL }} # 钉钉机器人地址
        QQ_SEND: ${{ secrets.QQ_SEND }} # qq发件人信息格式  邮箱+smtp码 比如：iui9@qq.com+********(加号为分隔符)
        QQ_ACCEPT: ${{ secrets.QQ_ACCEPT }} # qq收件人邮箱地址
        SERVER_SCKEY: ${{ secrets.SERVER_SCKEY }}  # server酱key密钥

      run: |
        python csdn/csdn.py