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


class comandi:
    def __init__(self, client):
        self.client = client

# пинг понг бля
    @commands.command()
    async def ping(self):
        await self.client.say('понг бля')

# постит цитатку из доты
    @commands.command()
    async def dota(self):
        # взять цитату из файла
        await self.client.say(random.choice(list(open('dota.txt', encoding="utf-8"))))

# выбор среди нескольких вариантов через пробел
    @commands.command()
    async def pick(self, *choices: str):
        await self.client.say(random.choice(choices))

# пишет что ты пидор
    @commands.command()
    async def ты(self):
        await self.client.say(random.choice(list(open('pidor.txt', encoding="utf-8"))))

def setup(client):
    client.add_cog(comandi(client))