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

class pic():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def pic(self, ctx, *, user: discord.Member=None):
     if user is None:
        usuario = ctx.author.avatar_url
        texto = f"Olá {ctx.author.name}, esta é o seu avatar"
     else:
         usuario = user.avatar_url
         texto = f"Olá {ctx.author.name}, esta é o avatar o {user.name}"

     embed = discord.Embed(title=texto, color=0xF4CBD1)
     embed.set_image(url=usuario)
     embed.set_footer(text="pic © {} hora {}".format(ano(),hora()))
     await ctx.send(embed=embed)


def setup(client):
    print("[Comando pic] Carregado")
    client.add_cog(pic(client))
