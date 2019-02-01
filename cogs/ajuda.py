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

class tradutor():
   def __init__(self, client):                            
       self.client = client

class ajuda():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ajuda(self, ctx):

       embed=discord.Embed(title=f"Esses são os meus cmds ", description=" ")
       embed.add_field(name="Musica 🔊", value="`seus cmds de musica`", inline=False)
       embed.add_field(name="Diversão😃 ", value="`seus cmds de diversão`", inline=False) 
       embed.add_field(name="Economia 💰 ", value="`seus cmds de economia`", inline=False)
       embed.add_field(name="Comandos que podem ajudar !", value="`seus cmds de que possam ajudar`", inline=False)
       await ctx.send(embed=embed)

def setup(client):
    print("[Comando ajuda] Carregado")
    client.add_cog(ajuda(client))
