import botpy
from botpy.message import Message
from botpy import logging, BotAPI
from botpy.ext.command_util import Commands
from openai import OpenAI
from config import Config

openAIClient = OpenAI(
    api_key=Config.OPENAI_APIKEY
)

openAIModel = Config.OPENAI_MODEL

if Config.OPENAI_BASEURL != "":
    openAIClient.base_url = Config.OPENAI_BASEURL

_log = logging.get_logger()


@Commands(name=("gpt"))
async def gpt(api: BotAPI, message: Message, params=None):
    _log.info(params)
    completion = openAIClient.chat.completions.create(
        model=openAIModel,
        messages=[
            {"role": "user", "content": params}
        ]
    )

    replyMessage = completion.choices[0].message.content
    _log.info(replyMessage)
    await message.reply(content=replyMessage)
    # await api.post_message(channel_id=message.channel_id, content=params, msg_id=message.id)
    return True


class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        handlers = [
            gpt,
        ]
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return


intents = botpy.Intents(public_guild_messages=True)
client = MyClient(intents=intents)
client.run(appid=Config.QQBOT_APPID, token=Config.QQBOT_TOKEN)
