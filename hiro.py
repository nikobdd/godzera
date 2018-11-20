import discord
import time
import datetime
import safygiphy
import asyncio



g = safygiphy.Giphy ()
color = 0x1ac8ff
start_time = {"start_time1": time.time ()}



client = discord.Client ()
imagem = {'000000000000000000': {'imagem': 0}}
thumbnail = {'000000000000000000': {'thumbnail': 0}}
cor = {'000000000000000000': {'color': '0x00000'}}

@client.event
async def on_ready():
        print(client.user.name)
        while True:
            await client.change_presence(game=discord.Game(name="Hiro 白", type=1, url='https://www.twitch.tv/zerotwo'),status='streaming')
            await asyncio.sleep(20)

            await client.change_presence(game=discord.Game(name="{} Usuários ".format(str(len(set(client.get_all_members())))), type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
            await asyncio.sleep(20)


@client.event
async def on_message(message):
        if message.content.startswith('h!setar'):
            set1 = message.content.strip('h!setar')
            imagem[message.author.id] = {'imagem': set1}
            embed1 = discord.Embed(color=color)
            embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
            embed1.add_field(name=f"{message.author.name}",value="**Pronto! coloquei a imagem que você pediu para ser enviada no DM dos membros! Digite (h!thumbnail + (link) para definir o icone**", inline=False)
            embed1.set_footer(text=message.server.name, icon_url=message.server.icon_url)
            embed1.timestamp = datetime.datetime.utcnow()
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed1)
        if message.content.startswith('h!thumbnail'):
            set1 = message.content.strip('h!thumbnail')
            thumbnail[message.author.id] = {'thumbnail': set1}
            embed1 = discord.Embed(color=color)
            embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
            embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
            embed1.add_field(name=f"{message.author.name}", value="**Pronto! coloquei a thumbnail que você pediu para ser enviada no DM dos membros\n Digite (h!dm) Para mandar a mensagem**", inline=False)
            embed1.timestamp = datetime.datetime.utcnow()
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed1)
        if message.content.lower().startswith('h!dm'):
            if not message.author.server_permissions.administrator:
                embed3 = discord.Embed(title="Negado Sem Permissão", description="**Você precisa ser um doador para usar este comando!\nprocure um ajudante no suporte da Zero Two para conseguir logo o seu Diamante**", color=color)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_image(url="https://cdn.discordapp.com/emojis/487745223133364224.png?v=1")
                embed3.timestamp = datetime.datetime.utcnow()
                return await client.send_message(message.channel, embed=embed3)
            msg = message.content.strip('h!dm')
            embed2 = discord.Embed(title='Enviando mensagem...', description='\n' + (msg), color=color)
            embed2.set_thumbnail( url="https://cdn.discordapp.com/emojis/489775219339165703.gif?v=1")
            embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=embed2)
            x = list(message.server.members)
            s = 0
            for member in x:
                user = message.author.name
                horario = datetime.datetime.now().strftime("%H:%M:%S")
                embed1 = discord.Embed(title="Hiro 白", url="", color=color, description='**• Mensagem nova pra você <a:cursor:495599239758348288>**\n<@{}>\n\n **• Enviado do Servidor <:coroa:487745226136485889>**\n **{}**\n\n**• Mensagem <a:bloblove:475826454492348425>**\n\n{}'.format(member.id, message.server.name, msg))
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
            embed2.set_thumbnail( url="https://cdn.discordapp.com/emojis/487745242640941069.gif?v=1")
            embed2.set_footer(text=message.server.name, icon_url=message.server.icon_url)
            embed2.timestamp = datetime.datetime.utcnow()
            await client.send_message(message.channel, embed=embed2)


client.run(str(os.environ.get('TOKEN')))
