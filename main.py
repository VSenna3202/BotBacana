import discord
import asyncio

client = discord.Client()


#Comando para iniciar
@client.event
async def on_ready():
    print(f'Bot {client.user.name} online\nHello world!')
    print(f'id do bot: \n{client.user.id}')
    await client.change_presence(activity=discord.Streaming(name='Eita', url='https://twitch.tv/Kl3t1n'))


#Comando de texto e prefixo
@client.event
async def on_message(message):
    if message.content.startswith('$'):
        mention = message.author.mention
        await message.channel.send(f'Bodia {mention}')



#Comando para colocar o Token Do Bot
client.run("token")
