import discord
import time
import datetime
import safygiphy
import asyncio
import os
import io


g = safygiphy.Giphy ()
color = 0xf781c6
start_time = {"start_time1": time.time ()}



client = discord.Client ()
imagem = {'000000000000000000': {'imagem': 0}}
thumbnail = {'000000000000000000': {'thumbnail': 0}}
cor = {'000000000000000000': {'color': '0x00000'}}

@client.event
async def on_ready():
        print(client.user.name)
        while True:
            await client.change_presence(game=discord.Game(name="Lunna Crystal", type=1, url='https://www.twitch.tv/zerotwo'),status='streaming')
            await asyncio.sleep(20)

            await client.change_presence(game=discord.Game(name="Procurando meu gatinho 🐱", type=1, url='https://www.twitch.tv/zerotwo'),status='streaming')
            await asyncio.sleep(20)
                
            await client.change_presence(game=discord.Game(name="{} Usuários ".format(str(len(set(client.get_all_members())))), type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
            await asyncio.sleep(20)


@client.event
async def on_message(message):
        if message.content.startswith('lu!setar'):
            set1 = message.content.strip('lu!setar')
            imagem[message.author.id] = {'imagem': set1}
            embed1 = discord.Embed(color=color)
            embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
            embed1.add_field(name=f"{message.author.name}",value="**Pronto! coloquei a imagem que você pediu para ser enviada no DM dos membros! Digite (lu!thumbnail + (link) para definir o icone**", inline=False)
            embed1.set_footer(text=message.server.name, icon_url=message.server.icon_url)
            embed1.timestamp = datetime.datetime.utcnow()
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed1)
        if message.content.startswith('lu!thumbnail'):
            set1 = message.content.strip('lu!thumbnail')
            thumbnail[message.author.id] = {'thumbnail': set1}
            embed1 = discord.Embed(color=color)
            embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
            embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
            embed1.add_field(name=f"{message.author.name}", value="**Pronto! coloquei a thumbnail que você pediu para ser enviada no DM dos membros\n Digite (lu!dm) Para mandar a mensagem**", inline=False)
            embed1.timestamp = datetime.datetime.utcnow()
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed1)
        if message.content.lower().startswith('lu!dm'):
            if not message.author.server_permissions.administrator:
                embed3 = discord.Embed(title="Negado Sem Permissão", description="**Você precisa ser um doador para usar este comando!\procure um ajudante no suport Lunna para conseguir logo o seu Crystal**", color=color)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_image(url="https://cdn.discordapp.com/emojis/518029263794995210.png?v=1")
                embed3.timestamp = datetime.datetime.utcnow()
                return await client.send_message(message.channel, embed=embed3)
            msg = message.content.strip('lu!dm')
            embed2 = discord.Embed(title='Enviando mensagem...', description='\n' + (msg), color=color)
            embed2.set_thumbnail( url="https://cdn.discordapp.com/emojis/518131518309400586.png?v=1")
            embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed2)
            x = list(message.server.members)
            s = 0
            for member in x:
                user = message.author.name
                horario = datetime.datetime.now().strftime("%H:%M:%S")
                embed1 = discord.Embed(title="Lunna Crystal", url="", color=color, description='**• Mensagem nova pra você <:amavel:518062801860952076>**\n<@{}>\n\n **• Enviado do Servidor <:policia:518062799847424022>**\n **{}**\n\n**• Mensagem <:banho:518131521832353792>**\n\n{}'.format(member.id, message.server.name, msg))
                embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
                embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
                embed1.set_footer(text="Enviado por --> {} • Hoje às {}".format(user, horario))
                try:
                    await client.send_message(member, embed=embed1)
                    print(member.name)
                    s += 1
                except:
                    pass
            print('\nAviso enviado para {} membros de {}'.format(s, len(x)))
            embed2 = discord.Embed(title='Concluido', color=color,description='\nAviso enviado para **{}** de **{}**'.format(s,len(x)))
            embed2.set_thumbnail( url="https://cdn.discordapp.com/emojis/518131518301011979.png?v=1")
            embed2.set_footer(text=message.server.name, icon_url=message.server.icon_url)
            embed2.timestamp = datetime.datetime.utcnow()
            await client.send_message(message.channel, embed=embed2)


client.run(str(os.environ.get('TOKEN')))
