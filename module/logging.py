import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import random
import datetime
import traceback
import psutil
import os


class logging:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        author = message.author
        content = message.content
        print('{}: {}'.format(author, content))
        await self.client.process_commands(message)


def setup(client):
    client.add_cog(logging(client))
