import discord
from discord.ext import commands
import time
import asyncio
import random
from discord import opus
import itertools
import sys
import traceback
from async_timeout import timeout
import datetime
from googletrans import Translator
import requests
import json


COR = 0x2977FF

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




   @commands.command()
   async def tbr(self, ctx, *, palavra=None):
       if palavra is None:
           embed2 = discord.Embed(title='Digite Uma Palavra',color=COR)
           embed2.add_field(name='Exemplo:',value='s!traduzir inside')
           embed2.set_footer(text="pic © {} hora {}".format(ano(),hora()))

           await ctx.send(embed=embed2)
       else:
           translator = Translator()
           req = translation = translator.translate(f'{palavra}', dest='pt')
           embed4 = discord.Embed(title='Sua Tradução',color=COR)
           embed4.add_field(name='Traduzida Para o Português Brasileiro',value=translation.text)
           embed4.set_footer(text="tradutor © {} hora {}".format(ano(),hora()))
           await ctx.send(embed=embed4)













def setup(client):
    print("[Tradutor] Carregado.")
    client.add_cog(tradutor(client))
