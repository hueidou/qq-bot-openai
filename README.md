# qq-bot-openai

## 使用

### 配置文件

配置按优先级

* 环境变量
* config.py

|配置项|说明|备注|
|---|---|---|
|OPENAI_APIKEY|openai apikey||
|OPENAI_BASEURL|接口代理或兼容openai的接口地址，非网络代理地址|可为空，未测试|
|QQBOT_APPID|AppID (机器人ID)||
|QQBOT_TOKEN|Token(机器人令牌)||

## 开发

```sh
# python3.11环境
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r ./requirements.txt
# 创建.env文件配置
cp .env.example .env
python app.py
```
