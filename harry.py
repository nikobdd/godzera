import random
import discord
import asyncio
import json
import time
import datetime
import safygiphy
import io
import os
import requests

client = discord.Client()
g = safygiphy.Giphy ()
color = 0x070404


imagem = {'000000000000000000': {'imagem': 0}}
thumbnail = {'000000000000000000': {'thumbnail': 0}}

@client.event
async def on_ready():
    while True:
        await client.change_presence(game=discord.Game(name="{} Usuários".format(str(len(set(client.get_all_members())))), type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
        await asyncio.sleep(10)

        await client.change_presence(game=discord.Game(name="Hogwarts", type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
        await asyncio.sleep(10)
        # Ele vai esperar 60 segundos para mudar para o proximo status
        await client.change_presence(game=discord.Game(name="The Hell Ψ roubou minha varinha", type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
        await asyncio.sleep(10)

        await client.change_presence(game=discord.Game(name="Luuh staff mais dlc", type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        
        
@client.event
async def on_message(message):      
    if message.content.startswith('+setimage'):
         set1 = message.content.strip('+setimage')
         imagem[message.author.id] = {'imagem': set1}
         embed1 = discord.Embed(color=color)
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="👷 Pronto, senhor(a) coloquei a imagem que você pediu para ser enviada no DM dos membros\n💎 Digite +setthumbnail (link)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.startswith('+setthumbnail'):
         set1 = message.content.strip('+setthumbnail')
         thumbnail[message.author.id] = {'thumbnail': set1}
         embed1 = discord.Embed(color=color)
         embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="Pronto, senhor(a) 👑 coloquei a thumbnail que você pediu para ser enviada no DM dos membros\n💎 Digite +msg)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.lower ().startswith ( '+msg' ):
        role = discord.utils.get(message.server.roles, name='Argo Filch')
        if not role in message.author.roles:
         embed1 = discord.Embed(title="SEM PERMISSÃO", description="Você precisa do cargo ADM",color=color)
         return await client.send_message(message.channel, embed=embed1)
        msg = message.content.strip ( '+msg')
        embed2 = discord.Embed(title='ENVIANDO MENSAGEM...',description='🚩 `MENSAGEM ESCOLHIDA:`\n' + (msg),color=color)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message(message.channel, embed=embed2)
        x = list ( message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed ( title="Hogwarts", url="", color=color,description=' <@{}> {}'.format(member.id, msg))
            embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
            embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
            embed1.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
            try:
                await client.send_message ( member, embed=embed1 )
                print ( member.name )
                s += 1
            except:
                pass
        print ( '\nAviso enviado para {} membros de {}'.format ( s, len ( x ) ) )
        embed2 = discord.Embed ( title='MENSAGEM ENVIADA:',description="📥 `SUCESSO:` \nMensagem enviada com sucesso para todos membros do servidor",color=color)
        embed2.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message ( message.channel, embed=embed2 )
        

        
    if message.content.startswith ( '+uptime' ):
        await client.send_message ( message.channel,"***Estou online a {0} hora(s) e {1} minuto(s)***".format(hour, minutes))

    async def tutorial_uptime():
        await client.wait_until_ready ()
        global minutes
        minutes = 0
        global hour
        hour = 0
        while not client.is_closed:
            await asyncio.sleep ( 60 )
            minutes += 1
            if minutes == 60:
                minutes = 0
                hour += 1

    client.loop.create_task (tutorial_uptime ())        
        
        
     
    if not (not message.content.startswith ( '+fale' ) and not message.content.startswith ( '+falar' )):
        if message.author.id == 'ID DO BOT':
            return
        try:
            mensagem = message.content[7:]
            await client.delete_message ( message )
            await client.send_message ( message.channel, mensagem, tts=False )
            print ( 'Fale on' )
            print ( mensagem )
        except:
            await client.send_message ( message.channel, "Você precisa escrever algo para eu falar!" )    
    
    
    
    if message.content.startswith('+gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(str(rgif.get("data", {}).get('image_original_url')), stream=True)
        embed = discord.Embed(color=color, description="<:PandaAdmireWizard:479054756476747786> Só Um Minuto Bruxo(a) O Gif Já Irá Aparecer")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/478270755831021588.png?v=1")
        embed.set_footer(text=message.server.name, icon_url=message.server.icon_url)
        await client.send_message(message.channel, embed=embed)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')
		    
    
  
    if message.content.lower().startswith('+aviso'):
        if not message.author.server_permissions.manage_messages:
            embed1 = discord.Embed(description=":no_good: **Sem Permissão!**", color=color)
            embed1.set_thumbnail(url="https://cdn.discordapp.com/emojis/478264373203173397.png?v=1")
            embed1.set_footer(text=client.user.name,icon_url="https://cdn.discordapp.com/emojis/478264373203173397.png?v=1")
            return await client.send_message(message.channel, embed=embed1)
        try:
            embed = discord.Embed(color=color, description="{}".format(message.content[7:]))
            embed.set_footer(text=message.server.name, icon_url=message.server.icon_url)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            pass
 


        
@client.event
async def on_member_join(member):
  embed1 = discord.Embed(color=color, description='***Hogwarts***')
  embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
  embed1 = discord.Embed ( title="\n<:hogwarts2:478401396639793162> Escola de Magia e Bruxaria De Hogwarts <:hogwarts2:478401396639793162>\n", url="", color=color,description='***\nDiretor: Albus Dumbledore\n Coordenadores das casas Grifinória, Sonserina, Lufa lufa, Corvinal\n\n\n*** Prezado(a) {}'.format(member.mention))
  embed1.add_field(name="***\n👻Temos o prazer de informar que você foi aceito na escola de Magia e Bruxaria de Hogwarts.👻***",value="*** Estamos anexando uma lista dos livros e equipamentos necessários para se matricular 📝, vá nos canais de voz (Expresso) 🔊 e entre em contato com algum Chapéu Seletor ou Elfo Doméstico 🎩, caso queria realizar sua matrícula por voz, basta responder as perguntas da <#478187966473306119> compre seu material aqui  <#481992231662649364> Torne-se o bruxo(a) mais poderoso da história!🔮\n\n\n ✨Atenciosamente;\n\n\n <:PandaAdmireWizard:479054756476747786>DIRETORIA DE HOGWARST<:PandaAdmireWizard:479054756476747786>***",inline=False)
  embed1.set_image(url="https://cdn.discordapp.com/attachments/479093968139976706/484127778107686924/logo22.png")
  await client.send_message(member,embed=embed1)



client.run(str(os.environ.get('TOKEN')))
