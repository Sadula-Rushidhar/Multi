from pyrogram import Client
from aiohttp import web
from plugins import web_server
from variables import *

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.id = me.id
       self.name = me.first_name
       self.mention = me.mention
       self.username = me.username
       #web-response
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, PORT).start()
       print(f'{me.first_name} is Started...🍃')

    async def stop(self, *args):
       await super().stop()      
       print("Bot restarting.....")
        
                           
  
bot = App()
bot.run()


        










