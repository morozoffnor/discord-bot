import discord
from discord.ext import commands
import giphypop
from giphypop import screensaver


class gifs:
    def __init__(self, client):
        self.client = client
# TODO поменять на сёрч потому что эта хуйня уже не поддерживается, оказывается бля)
    @commands.command()
    async def gif(self, text: str):
        scr = screensaver(text, api_key='t99aoKqUEvmafLWkqBD9zb04BlNiWXPJ')
        await self.client.say(scr)


def setup(client):
    client.add_cog(gifs(client))
