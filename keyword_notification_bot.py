import discord
import asyncio
import os

TOKEN = os.environ.get('BOT_TOKEN')
COMMAND = '!keyword'

keywords = {}

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for keyword in keywords:
        if keyword in keywords and keyword in message.content:
            msg = 'Keyword mentioned: {0.content}'.format(message)
            user = keywords[keyword]
            await client.send_message(user, msg)

    if message.content.startswith(COMMAND):
        new_keyword = message.content[len(COMMAND) + 1:]
        msg = 'Set notifications for keyword: {0}'.format(new_keyword)
        keywords[new_keyword] = message.author
        await client.send_message(message.author, msg)

client.run(TOKEN)
