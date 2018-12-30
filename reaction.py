import discord
import asyncio
import os

client = discord.Client ()
COR =0xe9f700
msg_id = None
msg_user = None

@client.event
async def on_ready():
        print(client.user.name)
        while True:
            await client.change_presence(game=discord.Game(name="Role Reaction TL", type=1, url='https://www.twitch.tv/zerotwo'),status='streaming')
            await asyncio.sleep(20)

            await client.change_presence(game=discord.Game(name="New Reaction", type=1, url='https://www.twitch.tv/zerotwo'),status='streaming')
            await asyncio.sleep(20)
                
            await client.change_presence(game=discord.Game(name="{} Usuários ".format(str(len(set(client.get_all_members())))), type=1,url='https://www.twitch.tv/ocupidex'), status='streaming')
            await asyncio.sleep(20)



@client.event
async def on_message(message):
    if message.content.lower().startswith("tl!staff"):
     embed1 =discord.Embed(
        title="Teste Staff TL!",
        color=COR,
        description="• Staff Evento = 🎉\n"
                    "• Staff Registro  =  📝 \n"
                    "• Staff Divulgação  =  📣 \n"
                    "• Staff Designer  =  🎨 \n"
                    "• Staff Organização  = 🎓",)

    botmsg = await client.send_message(message.channel, embed=embed1)

    await client.add_reaction(botmsg, "🎉")
    await client.add_reaction(botmsg, "📝")
    await client.add_reaction(botmsg, "📣")
    await client.add_reaction(botmsg, "🎨")
    await client.add_reaction(botmsg, "🎓")



    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🎉" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de evento", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📝" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de registro", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📣" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de divulgação", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🎨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de designer", msg.server.roles)
     await client.add_roles(user, role)
     print("add")
 

    if reaction.emoji == "🎓" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de organização", msg.server.roles)
     await client.add_roles(user, role)
     print("add")
 

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🎉" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de evento", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "📝" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de registro", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "📣" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de divulgação", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")


    if reaction.emoji == "🎨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de designer", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")



    if reaction.emoji == "🎓" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "quero ser staff de organização", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")     


client.run(str(os.environ.get('TOKEN')))
