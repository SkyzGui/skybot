﻿####################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################
import discord
from discord.ext import commands
import datetime

####################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################

def time():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M - %d/%m/%Y"))

def hora():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M"))

def ano():
    now = datetime.datetime.now()
    return (now.strftime("%Y"))

class botinfo():
    def __init__(self, bot):
        self.bot = bot

####################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################################################################################################

    @commands.command()
    async def botinfo(self , ctx):


       embed=discord.Embed(title="Botinfo", description="Essas são minhas informações")
       embed.add_field(name="<:ladoe:530100840707653633>Nome do bot", value=f"🔹`-_-SkyBot-_-`", inline=False)
       embed.add_field(name="<:ladoe:530100840707653633>Id do bot", value=f"🔹516991068521103372", inline=True)
       embed.add_field(name="<:ladoe:530100840707653633>Meu dono", value=f"🔹<@409821602012856321>", inline=False)
       embed.add_field(name="<:ladoe:530100840707653633>Meu prefixo", value=f"🔹`s!`", inline=True)
       embed.add_field(name="<:ladoe:530100840707653633>id do meu dono", value=f"🔹`409821602012856321`", inline=False)
       embed.add_field(name="<:ladoe:530100840707653633>Eu tenho", value=f"🔹`10`cmds caso queire saber quais são digite s!ajuda", inline=True)
       embed.add_field(name="<:ladoe:530100840707653633>Meu ping", value=f"🔹`{int(self.bot.latency  * 1000)}ms` ou digite `s!ping`", inline=False)
       embed.add_field(name="<:ladoe:530100840707653633>Estou hospedado na", value=f"🔹heroku <:heroku:530070832450502675>", inline=True)
       embed.set_footer(text="Botinfo © {} hora {}".format(ano(),hora()))
       await ctx.send(embed=embed)


########-############################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################################################################################################

def setup(bot):
    bot.remove_command("help")
    print("[comando botinfo] carregado")
    bot.add_cog(botinfo(bot))

####################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################################################################################################