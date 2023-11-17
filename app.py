import botpy
from botpy.message import Message
from botpy import logging, BotAPI
from botpy.ext.command_util import Commands
from openai import OpenAI
openAIclient = OpenAI(
    api_key="",
    base_url= ""
)

_log = logging.get_logger()

@Commands(name=("gpt"))
async def gpt(api: BotAPI, message:Message, params=None):
    _log.info(params)
    completion = openAIclient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": params}
        ]
    )

    replyMessage = completion.choices[0].message
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
client.run(appid="", token="")
