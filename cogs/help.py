import discord
from discord.ext import commands

class help():
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):

         def check(reaction, user):
             return user == message.author and str(reaction.emoji) == '👍'

         try:
             reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
         except asyncio.TimeoutError:
             await channel.send('👎')

def setup(client):
    print("[Comando help] Carregado")
    client.add_cog(help(client))
