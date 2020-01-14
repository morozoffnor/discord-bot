import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import random

# токен для бота
TOKEN = 'token'

# префикс-символ, который нужно ставить перед командой
client = commands.Bot(command_prefix='.')

extensions = ['module.comandi', 'module.gifs', 'module.twitch']

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} не может быть загружен. [{}]'.format(extension, error))


@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Модуль {} загружен'.format(extension))
        await client.say('Модуль {} загружен'.format(extension))
    except Exception as error:
        print('Модуль {} не может быть загружен. [{}]'.format(
            extension, error))
        await client.say('Модуль {} не может быть загружен. [{}]'.format(
            extension, error))


@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Модуль {} отключен'.format(extension))
        await client.say('Модуль {} отключен'.format(extension))
    except Exception as error:
        print('Модуль {} не может быть отключен. [{}]'.format(
            extension, error))
        await client.say('Модуль {} не может быть отключен. [{}]'.format(
            extension, error))


# "бот готов к работе"
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# пишет в консоль сервера, к которым подключен бот


async def servers_status():
    await client.wait_until_ready()

    while not client.is_closed:
        servers = list(client.servers)
        print('------')
        print('Connected on', str(len(client.servers)), 'servers:')
        for x in range(len(servers)):
            print(' ', servers[x - 1].name)
        print('------')
        await asyncio.sleep(9999)


# смена статуса бота каждые х секунд в фоне


async def change_status():
    await client.wait_until_ready()  # ждет, пока бот запустится

    while not client.is_closed:
        current_status = (random.choice(
            list(open('status.txt', encoding="utf-8"))))  # взять статус из файла
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(1000)  # менять статус каждые х секунд


# выводит в консоль сообщения от всех пользователей
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)


@client.command()
async def info(a: str):
    if a == ('подкаст'):
        await client.say('Душный подкаст — vk.com/stuffycast')
    elif a == ('Подкаст'):
        await client.say('Душный подкаст — vk.com/stuffycast')
    elif a == ('Podcast'):
        await client.say('Душный подкаст — vk.com/stuffycast')
    elif a == ('podcast'):
        await client.say('Душный подкаст — vk.com/stuffycast')


# бот повторяет за пользователем
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

# порно
@client.command()
async def porn(kakaha: str):
    if kakaha == 'jenre':
        await client.say('тут я напишу жанр')
    elif kakaha == 'actress':
        await client.say('тут я напишу актрису')
    else:
        await client.say('пока что я могу посоветовать актрису (.porn actress) или жанр (.porn jenre)')

client.loop.create_task(servers_status())  # раз в три часа инфа о серверах
client.loop.create_task(change_status())  # залупленная задача на смену статуса
client.run(TOKEN)
