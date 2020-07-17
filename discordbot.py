import discord
import asyncio
import random
import sys
import os

client = discord.Client()


@client.event
async def on_ready():
    print('-----Logged in info-----')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    test_blacklist = 0
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == '/test blacklist':
        test_blacklist = 1
        await message.channel.send('ブラックリストかどうか検知するよ！！')

    if message.content == 'わんこ！':
        await message.channel.send(f'{message.author.mention} なーに？？(｀･ω･´)✨')


client.run(os.environ.get('ENV_VAR_DISCORD_ID'))
