from discord.ext import commands
import os
import traceback
import discord

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(m):
    if m.guild.id == 796546441702932481:
        id = 863323034806386688
        chnnel = await client.fetch_channel(id)
        await channel.send(f'{m.channel.name}\n{m.author.name}\n\n{m.content}')

client.run(token)
