import discord
from discord.ext import commands
import datetime

def time():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M - %d/%m/%Y"))

def hora():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M"))

def ano():
    now = datetime.datetime.now()
    return (now.strftime("%Y"))

class ping():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self, ctx, *, user: discord.Member=None):

       embed=discord.Embed(title="PONG", description=" Veja meu ping! ")
       embed.add_field(name="Meu ping é aproximadamente", value=f"`{int(self.client.latency  * 1000)} ms` <a:ping:512065320320761867> ", inline=False)
       embed.set_footer(text="ping © {} hora {}".format(ano(),hora()))
       await ctx.send(embed=embed)

def setup(client):
    print("[Comando ping] Carregado")
    client.add_cog(ping(client))
