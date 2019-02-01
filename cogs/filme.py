import discord
from discord.ext import commands
import requests
import json

class filme():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def filme(self, ctx, *, buscar=None):

        if buscar is None:
           await ctx.send(f"{ctx.author.mention}, vc precisa colocar o nome de um filme exemplo ```s!filme matrix```")
           return

        buscar = str(buscar).replace(" ", "%20")
        r = requests.get(f'www.omdbapi.com/?i=tt3896198&apikey=1620539a&t={buscar}')
        if r.status_code == 200:
           js = r.json()

        embed=discord.Embed(title="filme", color=0xffff00)
        embed.add_field(name="Nome do filme", value=str(js['Title']), inline=True)
        embed.add_field(name="ano do filme", value=str(js['Year']), inline=False)
        embed.add_field(name="O filme foi lançado em", value=str(js['Released']), inline=True)
        embed.add_field(name="Dzuração do filme", value=str(js['Runtime']), inline=False)
        embed.add_field(name="Genero do filme", value=str(js['Genre']), inline=True)
        embed.add_field(name="diretor(es) do filme", value=str(js['Director']), inline=False)
        embed.add_field(name="Atores", value=str(js['Actors']), inline=True)
        await ctx.send(embed=embed)


def setup(client):
    print("[Comando filme] Carregado")
    client.add_cog(filme(client))
