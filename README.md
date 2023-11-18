# qq-bot-openai

一个简单的QQ频道机器人，`/gpt`指令进行gpt问答。

## 使用

### 配置文件

配置按优先级

* 环境变量
* config.py

|配置项|说明|默认值|
|---|---|---|
|OPENAI_APIKEY|openai apikey||
|OPENAI_MODEL|openai model|gpt-3.5-turbo|
|OPENAI_BASEURL|接口代理或兼容openai的接口地址，非网络代理地址|空，使用openai默认|
|QQBOT_APPID|AppID (机器人ID)||
|QQBOT_TOKEN|Token(机器人令牌)||

### 运行

* 直接运行: `python app.py`
* Docker: `hueidou/qq-bot-openai:latest`
* Docker-Compose示例: `deploy/docker-compose/docker-compose.yml`
* Kubernetes示例: `deploy/k8s/qq-bot-openai.yaml`

## 开发

```sh
# python3.11环境
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r ./requirements.txt
# 创建.env文件配置
cp .env.example .env
python app.py
```
