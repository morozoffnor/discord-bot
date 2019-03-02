import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import random

# токен для бота
TOKEN = 'NTQ5NDk5MDgyMTY3ODEyMTA2.D1UxJQ.AWi7M3_4WKMf6zoT5Ydvp6_xRP8'

# префикс-символ, который нужно ставить перед командой
client = commands.Bot(command_prefix='.')

# "бот готов к работе"
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# пинг-понг команда
@client.command()
async def ping():
    await client.say('pong!')

# смена статуса бота каждые х секунд в фоне


async def change_status():
    await client.wait_until_ready()  # ждет, пока бот запустится

    while not client.is_closed:
        current_status = (random.choice(
            list(open('status.txt', encoding="utf-8"))))  # взять статус из файла
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(1000)  # менять статус каждые х секунд


# выводит в консоль сообщения от всех пользователей, кроме бота
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)

# постит пидора
@client.command()
async def ты():
    # взять пидора из файла
    await client.say(random.choice(list(open('pidor.txt', encoding="utf-8"))))


@client.command(description='For when you wanna settle the score some other way')
async def pick(*choices: str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))


# постит цитату из доты
@client.command()
async def dota():
    # взять цитату из файла
    await client.say(random.choice(list(open('dota.txt', encoding="utf-8"))))

# бот повторяет за пользователем
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.loop.create_task(change_status())  # залупленная задача на смену статуса
client.run(TOKEN)
