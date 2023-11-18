# config.py
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configuration with default values

class Config:
    OPENAI_APIKEY = os.getenv('OPENAI_APIKEY', '')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    OPENAI_BASEURL = os.getenv('OPENAI_BASEURL', '')
    QQBOT_APPID = os.getenv('QQBOT_APPID', '')
    QQBOT_TOKEN = os.getenv('QQBOT_TOKEN', '')

print(Config.OPENAI_APIKEY)
print(Config.OPENAI_MODEL)
print(Config.OPENAI_BASEURL)
print(Config.QQBOT_APPID)
print(Config.QQBOT_TOKEN)
