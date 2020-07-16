import csv
from typing import TextIO

import discord


# 自分のBotのアクセストークンに置き換えてください
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
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

    if message.attachments:
        for attachment in message.attachments:
            # Attachmentの拡張子がpng, jpg, jpegのどれかだった場合
            if attachment.url.endswith(("png", "jpg", "jpeg")):
                # await message.channel.send(attachment.url)
                await attachment.save("cat.png")
    # attachment = message.attachments[0]
    # 送られてきたファイルをattachment.pngという名前で保存する
    # await attachment.save("cat.png")
    if message.content == 'ねこ！':
        with open('test.csv') as s:
            row0 = [row for row in csv.reader(s)]
            print(row0)
            s.close()
        with open('test.csv', 'a') as s:
            # open('test.csv', 'w')だと上書きになる。
            writer = csv.writer(s)
            # writer.writerow([0, 1, 2])
            # writer.writerow(['a', 'b', 'e'])
            s.close()
        # import pandas as pd
        # df = pd.read_csv("test.csv", encoding='SHIFT_JIS')
        # df = df.drop[0]

    if message.content == '/test blacklist':
        test_blacklist = 1
        await message.channel.send('ブラックリストかどうか検知するよ！！')
    
    if message.content == 'わんこ！':
        await message.channel.send(f'{message.author.mention} なーに？？(｀･ω･´)✨')
        # await message.channel.send(file=discord.File("cat.png"))
    if test_blacklist == 1:
        with open('sample.csv', encoding='utf_8_sig') as f:
            for row in csv.reader(f):
                if row[0] == message.content:
                    await message.channel.send(row)
                print(row)
            # csvの要素取得… print([row for row in csv.reader(f)][要素の列][要素の行])
            # 行だけ取得したいときは転置行列を作る。
            # int()で整数値化できる
        # print(f.read())
    elif client.user in message.mentions:
        await message.channel.send(message.content.lower().translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})))
        # 文字を半角に…文字列.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        # 文字列を大文字に…文字列.upper()
        # 文字列を小文字に…文字列.lower()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
