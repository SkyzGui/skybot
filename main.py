import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or
import dados

client = AutoShardedBot(command_prefix=when_mentioned_or(dados.prefix()), case_insensitive=True)

@client.event
async def on_ready():
    print(f"Nenhum virus encontrado - Bot name {client.user.name} Id do bot encontrado ({client.user.id})")
    await client.change_presence(activity=discord.Streaming(name="digite s.ajuda", url="https://www.twitch.tv/nkoficial"))


def run_modules():

	try:
	  client.remove_command("help")
	  print("Um virus foi abatido -- comando help removido.")
	  for modulos in dados.modulos():
	  	 client.load_extension(modulos)
	  print(f"[Ok] nenhum virus detectado - {len(dados.modulos())} modulos carregados.")
	except Exception as e:
		print(f"Um virus foi detectado: O {modulos} Não foi carregado pelo motivo = {e}")

	try:
	  client.run(dados.token())
	  print(f"Nenhum virus foi detectado -- Bot foi carregado")
	except Exception as e:
		print(f"Um virus foi detectado: O bot não conseguiu se conectar ao discord  = {e}")

if __name__ == '__main__':
	run_modules()