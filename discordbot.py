from discord.ext import commands
import os
import traceback

client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == 'わんこ！':
        await message.channel.send(f'{message.author.mention} なーに？？(｀･ω･´)✨')
        # await message.channel.send(file=discord.File("cat.png"))


client.run(token)
