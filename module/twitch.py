import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import random
import datetime
import traceback
import psutil
import os

# инициализировать класс


class twitch:
    def __init__(self, client):
        self.client = client

# пинг понг бля
    @commands.command()
    async def twitch(self, user):
        if (user == 'GameOver.inc' or user == 'gameover' or user == 'gameover.inc' or user == 'Gameover' or user == 'гамовер' or user == 'гамова'):
            await self.client.say('Twitch-канал GameOver.inc — https://www.twitch.tv/gameover_inc')
        elif (user == 'suXin' or user == 'suxin' or user == 'Suxin' or user == 'SuXin' or user == 'схуин' or user == 'сухин' or user == 'Сухин' or user == 'Схуин'):
            await self.client.say('Twitch-канал suXin — https://www.twitch.tv/suXinjke')
        elif (user == 'morozoff' or user == 'Morozoff' or user == 'morozer' or user == 'morozoffplay' or user == 'MorozoffPlay' or user == 'морозер' or user == 'морозов' or user == 'Морозов'):
            await self.client.say('Twitch-канал morozoffplay — https://www.twitch.tv/morozoffplay')
        else:
            await self.client.say('Ты ввел какую-то чепуху, я не знаю таких стримеров. Попробуй ещё раз!')
            


def setup(client):
    client.add_cog(twitch(client))