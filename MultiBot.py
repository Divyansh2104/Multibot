import discord
from discord import embeds
from discord import colour
from discord.ext import commands
import random
import os
from PIL import ImageDraw, ImageFont, ImageFilter, Image
import asyncpraw
import asyncio
from io import BytesIO
import qrcode 


intents = discord.Intents.all()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="<prefix>")
bot.remove_command("help")




os.chdir()

filtered_words = ["fuck","nigg","cock","fuk","c0ck","cunt","cnut","bitch","Bitch","B!tch","b1tch","b!tch","dick","d1ck","pussy","asshole","blowjob","Fuck","Fuk"]    
Hello_words = ["Hi","Hello","Hii","Hemlo","Hey","hi","hello","hii","hemlo","hey"]
Hello_responses = ["Hello","Hi","Hii","Hey"]

@bot.event
async def on_ready():
    # Setting `Playing ` status
    await bot.change_presence(activity= discord.Game(name=f"-help| {len(bot.guilds)} servers!"))

    # Setting `Listening ` status
    await bot.change_presence(activity= discord.Activity(type= discord.ActivityType.listening, name= "-help"))

    
     

async def ch_pr():
    await bot.wait_until_ready()

    statuses = [f"-help| {len(bot.guilds)} servers!","-help"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity= discord.Game(name=status))
        

        await asyncio.sleep(10)    


#-------------------#
#---HELP COMMANDS---#
#-------------------# 

@bot.command(invoke_without_command=True)
async def help(ctx):
    url = ctx.author.avatar_url

    em = discord.Embed(title ="Help", description= "My prefix is `-`", color = discord.Color.random(),timestamp= ctx.message.created_at)

    em.add_field(name = "Moderation", value = "`Type -mod to view commands`", inline= True)
    em.add_field(name = "Fun", value = "`Type -fun to view commands`", inline= True)
    em.add_field(name = "Image", value = "`Type -image to view commands`", inline= True)
    em.add_field(name = "Utility", value = "`Type -utils to view commands`", inline= True)
    em.add_field(name = "More", value = "`Type -more to view commands`", inline= True)
    em.add_field(name= "Links", value= "[**Invite**](https://discord.com/api/oauth2/authorize?client_id=895890670756171777&permissions=8&scope=bot)\n[**Support Server**](https://discord.gg/WnEJYztgge)")
    em.set_footer(text= f"Requested By {ctx.author}", icon_url= url)

    
    
    await ctx.send(embed = em)






@bot.command(invoke_without_command=True, )
async def mod(ctx):
    url = ctx.author.avatar_url

    em = discord.Embed(title ="<:Moderator:899945459899043861> Moderation Commands", color = discord.Color.random(),timestamp= ctx.message.created_at)

    em.add_field(name = "ban", value = "`Ban a member from the server`", inline= True)
    em.add_field(name = "kick", value = "`Kicks a member from the server`", inline= True)
    em.add_field(name = "lock", value = "`Locks a channel`", inline= True)
    em.add_field(name = "unlock", value = "`Unlocks a locked channel`", inline= True)
    em.add_field(name = "hide", value = "`Make a channel private`", inline= True)
    em.add_field(name = "unhide", value = "`Make a channel public`", inline= True)
    em.add_field(name = "mute", value = "`Mutes a member until unmuted`", inline= True)
    em.add_field(name = "unmute", value = "`Unmutes the muted member`", inline= True)
    em.add_field(name = "addrole", value = "`Adds a role in the user's roles`", inline= True)
    em.add_field(name = "removerole", value = "`Removes a role  the user's roles`", inline= True)
    em.add_field(name = "say", value = "`Broadcast a message in the channel`", inline= True)
    em.add_field(name = "purge", value = "`Purge the number of messages`", inline= True)
    em.add_field(name = "nuke", value = "`Nukes a channel`", inline= True)
    em.add_field(name = "hide", value = "`Hides a channel`", inline= True)
    em.add_field(name = "unhide", value = "`Unhides a channel`", inline= True)
    em.add_field(name = "createrole", value = "`Creates a role`", inline= True)
    em.add_field(name = "slowmode", value = "`Sets the slowmode time for a channel`", inline= True)
    em.add_field(name = "ping", value = "`Shows the bot latency`", inline= True)    
    
    em.set_footer(text= f"Requested By {ctx.author}", icon_url= url)

    await ctx.send(embed = em)
   


@bot.command(invoke_without_command=True, )
async def fun(ctx):
    url = ctx.author.avatar_url
    em = discord.Embed(title ="<a:Pepe_Boom:894896251223547905> Fun Commands", color = discord.Color.random(),timestamp= ctx.message.created_at)

    em.add_field(name = "8ball", value = "`Answers your all questions`")
    em.add_field(name = "Meme", value = "`Shows you a noice meme`")
    em.add_field(name = "Emojify", value = "`Emojifies the given text`")
    em.add_field(name = "Truth", value = "`Truth Or Dare!`")
    em.add_field(name = "Dare", value = "`Truth Or Dare!`")
    em.add_field(name = "Coming Soon", value = "`Wait for it, more commands will be added here for you`")
    em.set_footer(text= f"Requested By {ctx.author}", icon_url= url)

    await ctx.send(embed = em)



@bot.command(invoke_without_command=True, )
async def image(ctx):
    url = ctx.author.avatar_url
    em = discord.Embed(title ="📷 Image Commands", color = discord.Color.random(),timestamp= ctx.message.created_at)

    em.add_field(name = "Wanted", value = "`Makes a wanted image of a user`")
    em.add_field(name = "Kill", value = "`Kills a user`")
    em.add_field(name = "Slap", value = "`Slaps a user`")
    em.add_field(name = "Punch", value = "`Punchs a user`")
    em.add_field(name = "RIP", value = "`Makes a rip image for a user`")
    em.add_field(name = "Minecraft", value = "`Gives you a minecraft advancement`")
    em.add_field(name = "Blur", value = "`Make a user's avatar blur`")
    em.add_field(name = "Beautiful", value = "`Make a beautiful image with a user's avatar`")
    em.add_field(name = "Versus", value = "`Make a versus image with 2 user's avatar`")
    em.set_footer(text= f"Requested By {ctx.author}", icon_url= url)

    await ctx.send(embed = em)  


@bot.command(invoke_without_command=True, )
async def more(ctx):
    url = ctx.author.avatar_url
    em = discord.Embed(color = discord.Color.random(),timestamp= ctx.message.created_at)

    em.add_field(name = "Servers", value = "`Shows the number of servers, the bot in`")
    em.add_field(name = "Invite", value = "`Gives you the bot invite link`")
    em.add_field(name = "Vote", value = "`Gives you a voting link for the bot`")
    
   
    em.set_footer(text= f"Requested By {ctx.author}", icon_url= url)

    await ctx.send(embed = em)


@bot.command(invoke_without_command= True)
async def perms(ctx):
    em = discord.Embed(title = "Permissions required for commands",color= discord.Color.random(),timestamp = ctx.message.created_at)

    em.add_field(name= "Commands",value= "Ban\nKick\nMute\nUnmute\nAddrole\nRemoverole\nLock\nUnlock\nHide\nUnhide\nPurge\nNuke")
    em.add_field(name= "Permissions", value="Ban Members\nKick Members\nKick Members\nKick Members\nManage Roles\nManage Roles\nManage Channels\nManage Channels\nManage Channels\nManage Channels\nManage Messages\nManage Channels")



    await ctx.send(embed = em)


@bot.command(invoke_without_command=True, )
async def utils(ctx):
    url = ctx.author.avatar_url
    em = discord.Embed(color = discord.Color.random(),timestamp= ctx.message.created_at)

    em.add_field(name = "Avatar", value = "`Shows a user's avatar`")
    em.add_field(name = "ID", value = "`Gives you a members ID`")
    em.add_field(name = "Membercount", value = "`Shows the number of members in the server`")
    em.add_field(name = "Servericon", value = "`Shows the server icon`")
    em.add_field(name = "Serverinfo", value = "`Tells the server's info`")
    em.add_field(name = "Whois", value = "`Tells a user's info`")
    em.add_field(name = "QrCode", value = "`Generates a qrcode of a link`")
   
    em.set_footer(text= f"Requested By {ctx.author}", icon_url= url)

    await ctx.send(embed = em)        




#---------------------------------#
#-------MODERATION COMMANDS-------#
#---------------------------------#

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member,*,reason=None):    
    if reason == None:
        await ctx.send("Please write a reason!")
        return
    
    await ctx.send(f"{member.name} have been banned from {ctx.guild} | Reason = {reason}")
    await member.ban(reason=reason)  




@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member,*,reason=None):
    if reason == None:
        await ctx.send("Please write a reason!")
        return

    await ctx.send(f"{member.name} have been kicked from {ctx.guild} | Reason = {reason}")
    await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx,amount=2):
    await ctx.channel.purge(limit=amount)


@bot.command(case_insensitive=True)
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member, *, reason=None):
    if reason == None:
        await ctx.send("Please write a reason!")
        return
    guild = ctx.guild
    muteRole= discord.utils.get(guild.roles, name= "Muted")    

    if not muteRole:
        await ctx.send("No 'Muted' Role Found, Creating One....")
        muteRole = await guild.create_role(name = "Muted")

        for channel in guild.channels:
            await channel.set_permissions(muteRole, speak=False, send_messages=False, read_messages=True, read_message_history=True)
        await member.add_roles(muteRole, reason=reason)
        await ctx.send(f"{member.mention} has been muted in {ctx.guild} | Reason : {reason}")
    else:
        await member.add_roles(muteRole, reason=reason)
        await ctx.send(f"{member.mention} has been muted in {ctx.guild} | Reason : {reason}")  
         




@bot.command(case_insensitive=True)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member, *, reason=None):
    
    guild = ctx.guild 
    muteRole= discord.utils.get(guild.roles, name= "Muted")

    if not muteRole:
        await ctx.send(f"{member.mention} is not muted!")
        return
    await member.remove_roles(muteRole)
    await ctx.send(f"{member.mention} has been unmuted successfully!")


@bot.command(aliases=["lock"])
@commands.has_permissions(manage_channels=True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"{ctx.channel.mention} is now locked successfully!")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"{ctx.channel.mention} is now unlocked successfully!")


@bot.command()
async def ping(ctx):
    em = discord.Embed(title= f"**{round(bot.latency * 100)} ms!**",color = discord.Color.random(), timestamp = ctx.message.created_at)
    em.set_author(name="🏓Pong!")
    await ctx.send(embed = em)


@bot.command(case_insensitive= True)
async def say(ctx, *,saymsg=None):
    if saymsg==None:
        return await ctx.send("Please enter 'something' you want the bot to say")
    await ctx.send(saymsg)


@bot.command()
@commands.has_permissions(manage_roles = True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"{role.mention} role given to {member.mention}✅")


@bot.command()
@commands.has_permissions(manage_roles = True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"{role.mention} role is now removed from {member.mention}✅")


@bot.command(case_insensitive = True)
@commands.has_permissions(manage_messages = True)
async def slowmode(ctx, time:int):
    if time == 0:
        await ctx.channel.edit(slowmode_delay = 0)
        await ctx.send("Channel slowmode is now set to `0` seconds")
    elif time > 21600:
        await ctx.send("You cannot set slowmode higher than 6 hours!")
        return
    else:
        await ctx.channel.edit(slowmode_delay = time)
        await ctx.send(f"Slowmode for {ctx.channel.mention} is now set to `{time}` seconds")


@bot.command(aliases=["cr"])
@commands.has_permissions(manage_roles=True)
@commands.bot_has_permissions(manage_roles=True)
async def create_role(ctx, *, role_name=None):
    if role_name == None:
        return await ctx.send(f"{ctx.author.mention}, Please enter the name for the role")

    New_Role = await ctx.guild.create_role(name = role_name)
    await ctx.send(f"Succesflly created the role with the name {role_name}!")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send(f"Succesfully made {ctx.channel.mention} a private channel!")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send(f"Succesfully made {ctx.channel.mention} a public channel!")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx,amount=99999**99999):
    await ctx.channel.purge(limit=amount)
    em = discord.Embed(title= f"This channel is nuked by {ctx.author}!", colour= discord.Color.random())
    em.set_image(url="https://c.tenor.com/hDJ1EV_X0AIAAAAC/vasu.gif")

    await ctx.send(embed=em)



#--------------------------#
#-------FUN COMMANDS-------#
#--------------------------# 

reddit = asyncpraw.Reddit(client_id= "<Your Reddit Apps ID>",
                        client_secret= "<Yout Reddit Apps Secret>",
                        username= "<Your Reddit Username>",
                        password= "<Password>",
                        user_agent= "<user_agent can be anything>")





all_subs = []


async def gen_memes():
    subreddit = await reddit.subreddit("memes")
    top = subreddit.top(limit = 200)
    async for submission in top:
      all_subs.append(submission)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has avoken")
    await gen_memes()  # generate memes when bot starts

@bot.command(aliases=['memes'])
async def meme(ctx):
    random_sub = random.choice(all_subs)
    all_subs.remove(random_sub)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)
    
    if len(all_subs) <= 20:  # meme collection running out owo
        await gen_memes()
       
        


@bot.command(aliases= ["8ball", "8b"])
async def eightball(ctx, *, question=None):
    if question==None:
        return await ctx.send("Please enter a question you wanna ask to 8ball")

    responses = [
        'Hell no.',
        'Subscribe To Gaming With Divyansh',
        'https://www.youtube.com/c/GamingWithDivyansh',
        'Prolly not.',
        'Idk bro.',
        'Prolly.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitaly.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Reply Hazy, Try again.',
        'IDK but u should subscribe to Gaming With Divyansh On Youtube',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']    
    await ctx.send(f":8ball: {random.choice(responses)}")



@bot.command()
async def emojify(ctx, *, text=None):
    if text == None:
        return await ctx.send("Please enter the text you wanna emojify")

    emojis = []
    for e in text.lower():
        if e.isdecimal():
            num2emo = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'} 



            emojis.append(f":{num2emo.get(e)}:")       
        elif e.isalpha():
            emojis.append(f":regional_indicator_{e}:")
        else:
            emojis.append(e)
    await ctx.send(" ".join(emojis))



@bot.command(aliases=["t"])
async def truth(ctx):
    Truths = ["Tell 1 people about your most akward moment",
    " If your parents went out of town for a week and you had the house to yourself, what would you do?",
    "Have you ever cheated to win a game?",
    "Tell one of your friend abour your girlfriend or crush"]

    await ctx.send(random.choice(Truths))

@bot.command(aliases=["d"])
async def dare(ctx):
    Dares= ["Change your profile pic for 2 days to whatever your friend says",
    "Call your crush or gf and say that you hate them",
    "Change your nickanme to whatever the group decide",
    "Ask anyone in the server to go out on a date with you",
    "Say your best friend that we are no longer friends [if he/she ask the reason doesn't say anything]",
    "Eat a snack without using hands",
    "Do a prank call on anyone",
    "Call your crush and make a conversation for at least 5 mins.",
    "Call your MOM ans say that you don't like her[btw Mother's are the best]",
    "Throw a bown on floor and run from your Mom",
    "Change your about me to whatever the group decides",
    "Bark like a dog in front of your neighbour's house",
    "Ring the bell and kick on the door of your neighbour's house",
    ]    
    await ctx.send(random.choice(Dares))


  


#---------------------------#
#-------IMAGE COMMANDS------#
#---------------------------#

@bot.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((358,358)) 

    wanted.paste(pfp, (70,166))

    wanted.save("wantedd.jpg")

    await ctx.send(file = discord.File("wantedd.jpg"))
    

    os.remove("wantedd.jpg")



@bot.command()
async def kill(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    kill = Image.open("Kill.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((201,201)) 

    kill.paste(pfp, (89,119))

    kill.save("killl.jpg")

    await ctx.send(file = discord.File("killl.jpg"))

    os.remove("killl.jpg")


@bot.command()
async def slap(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    slap = Image.open("slap.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((130,130)) 

    slap.paste(pfp, (301,119))

    slap.save("slapp.jpg")

    await ctx.send(file = discord.File("slapp.jpg"))

    os.remove("slapp.jpg")


@bot.command()
async def beautiful(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    Beauty = Image.open("Beauty.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((146,150)) 

    Beauty.paste(pfp, (335,31))

    pfp = pfp.resize((126,150))

    Beauty.paste(pfp, (344,329)) 

    Beauty.save("BEAUTYYY.jpg")

    await ctx.send(file = discord.File("BEAUTYYY.jpg"))

    os.remove("BEAUTYYY.jpg")            



 



@bot.command()
async def rip(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    RIP = Image.open("RIP.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((156,156)) 

    RIP.paste(pfp, (77,144))

    RIP.save("ripp.jpg")

    await ctx.send(file = discord.File("ripp.jpg"))        

    os.remove("ripp.jpg")



@bot.command()
async def punch(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    Punch = Image.open("Punch.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((247,247)) 

    Punch.paste(pfp, (38,24))

    Punch.save("punchh.jpg")

    await ctx.send(file = discord.File("punchh.jpg"))        

    os.remove("punchh.jpg")


@bot.command()
async def captcha(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    Cap = Image.open("Captcha.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((125,125)) 

    Cap.paste(pfp, (11,139))

    Cap.paste(pfp, (141,139))

    Cap.paste(pfp, (269,139))

    Cap.paste(pfp, (11,274))

    Cap.paste(pfp, (141,274))

    Cap.paste(pfp, (269,274))

    Cap.paste(pfp, (11,401))

    Cap.paste(pfp, (141,401))

    Cap.paste(pfp, (269,401))

    Cap.save("captchha.jpg")

    await ctx.send(file = discord.File("captchha.jpg"))        

    os.remove("captchha.jpg")


@bot.command()
async def blur(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    Blur = Image.open("Blur.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    pfp = pfp.resize((351,351)) 

    Blur.paste(pfp, (0,0))

    Blur.filter(ImageFilter.GaussianBlur(15)).save("blurr.jpg")


    await ctx.send(file = discord.File("blurr.jpg"))        

    os.remove("blurr.jpg")      

    
@bot.command()
async def minecraft(ctx, *, text = None):
    if text == None:
        return await ctx.send("Please enter a text")

    pics = ["MC1.jpg","MC2.jpg","MC3.jpg","MC4.jpg","MC5.jpg","MC6.jpg","MC7.jpg","MC8.jpg"] 
    img = Image.open(f"{random.choice(pics)}") 

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Mojang-Regular.ttf", 40) 

    draw.text((131,79), text, (255,255,255), font = font)

    img.save("Advancement.jpg")

    await ctx.send(file = discord.File("Advancement.jpg"))

    os.remove("Advancement.jpg")


@bot.command(aliases=["vs"])
async def versus(ctx, user: discord.Member = None):
    if user == None:
        return await ctx.send(f"{ctx.author.mention}, Please mention someone!")

    vs = Image.open("VS.jpg")  

    asset = user.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp = Image.open(data)

    asset = ctx.author.avatar_url_as(size = 128)   
    data = BytesIO(await asset.read()) 
    pfp2 = Image.open(data)

    pfp = pfp.resize((120,120))
    pfp2 = pfp2.resize((120,120))  

    vs.paste(pfp, (51,79))
    vs.paste(pfp2, (270,79))

    vs.save("VSVS.jpg")

    await ctx.send(file = discord.File("VSVS.jpg"))

    os.remove("VSVS.jpg")

#---------------------------#
#-------MORE COMMANDS-------#
#---------------------------#

@bot.command()
async def invite(ctx):
    em =discord.Embed() 

    em.add_field(name= "MUŁTI BØT Invite",value= "[**Click Here To Invite Me!**](https://discord.com/api/oauth2/authorize?client_id=895890670756171777&permissions=8&scope=bot)")      
    await ctx.send(embed= em)


@bot.command()
async def servers(ctx):

    await ctx.send(f"{ctx.author.mention} I am in {len(bot.guilds)} servers!")

@bot.command()
async def vote(ctx):
    em = discord.Embed(title= f"Vote For {bot.user.name}!", color= ctx.author.color, timestamp = ctx.message.created_at)

    em.set_thumbnail(url="https://w7.pngwing.com/pngs/207/931/png-transparent-ballot-box-voting-election-electoral-system-ballot-aarhus-voting-unicode-thumbnail.png")
    em.add_field(name="Top.gg", value="[**Click Here To Vote On Top.gg**](https://top.gg/bot/895890670756171777/vote)") 

    await ctx.send(embed = em)   
#-------------------------------#
#--------UTILITY COMMANDS-------#
#-------------------------------#


@bot.command(aliases=["userinfo"])
async def whois(ctx, *,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention) 

    b = ", ".join(rlist)


    embed = discord.Embed(colour= discord.Color.random(),timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}", icon_url= user.avatar_url),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'ID {user.id}')

    embed.add_field(name='**__Name__**',value=user,inline=False)
    embed.add_field(name='**__Nickname__**',value=user.display_name,inline=False)
    embed.add_field(name='**__Server Name__**',value=ctx.guild,inline=False)

    embed.add_field(name='**__Created at__**',value=user.created_at,inline=False)
    embed.add_field(name='**__Joined at__**',value=user.joined_at,inline=False)

    embed.add_field(name=f'**__Roles[{len(rlist)}]__**',value=''.join([b]),inline=False)
    embed.add_field(name='**__Top Role__**',value=user.top_role.mention,inline=False)

    embed.add_field(name='**__Bot__**',value=user.bot,inline=False)

    await ctx.send(embed=embed)



@bot.command()
async def serverinfo(ctx):
    url = ctx.guild.icon_url



    em = discord.Embed(color = discord.Color.random(), timestamp = ctx.message.created_at)
    em.set_thumbnail(url=url)

    em.add_field(name = "**__Server Name__**", value= ctx.guild,inline=False)
    em.add_field(name = "**__Region__**", value= ctx.guild.region,inline=False)
    em.add_field(name = "**__Owner__**", value= ctx.guild.owner ,inline=False)
    em.add_field(name = "**__Verification Level__**", value= ctx.guild.verification_level,inline=False)
    

    em.add_field(name = "**__Created On__**", value= ctx.guild.created_at,inline=False)

    
    em.add_field(name = "**__Member Count__**", value= ctx.guild.member_count,inline=False)
    em.add_field(name = "**__Role Count__**", value= len(ctx.guild.roles),inline=False)

    em.add_field(name = "**__Channels__**", value= len(ctx.guild.channels),inline=False)
    em.set_footer(text=f"ID {ctx.guild.id}")
    em.set_author(name= f"{ctx.guild} info", icon_url=url)

    
    
    await ctx.send(embed = em)


@bot.command(aliases=["av"])
async def avatar(ctx, *,user: discord.Member = None):
    if user == None:
        user = ctx.author

    url = user.avatar_url_as(size=128)

    em = discord.Embed(title = f"{user.display_name}'s avatar", color = discord.Color.random())
    em.set_image(url = url)  

    await ctx.send(embed = em) 

@bot.command()
async def servericon(ctx):

    url = ctx.guild.icon_url

    em = discord.Embed(title=f"{ctx.guild} icon",color = discord.Color.random(),timestamp = ctx.message.created_at)

    em.set_image(url = url)
    em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed = em)


@bot.command()
async def membercount(ctx):
    url = ctx.guild.icon_url

    em = discord.Embed(color = discord.Color.random(),timestamp = ctx.message.created_at) 
    em.set_author(name=f"{ctx.guild}", icon_url=url)

    em.add_field(name="Member Count", value=f"{ctx.guild.member_count}") 

    await ctx.send(embed=em)


@bot.command()
async def id(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author

    em = discord.Embed(color = discord.Color.random(), timestamp= ctx.message.created_at)

    em.set_author(name= f"{member.display_name}'s ID", icon_url=member.avatar_url)
    em.add_field(name="ID", value=member.id) 

    await ctx.send(embed=em)

@bot.command(aliases=["qrcode","qr"])
async def gen_qrcode(ctx, *, url=None):
    if url == None:
        return await ctx.send(f"{ctx.author.mention}, Please provide a url to make a qr code!")
    img = qrcode.make(url)
    img.save("QRCODE.jpg")
    await ctx.send(f"{ctx.author.mention}, Here's your qr code of the given link!",file = discord.File("QRCODE.jpg")) 
    os.remove("QRCODE.jpg")



@bot.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
            await msg.channel.send(f"{msg.author.mention} Watch Your Language")
            

    await bot.process_commands(msg)   


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    for word in Hello_words:
        if word in msg.content:
            await msg.channel.send(f"{msg.author.mention}, {random.choice(Hello_responses)}!")
            

    await bot.process_commands(msg) 
       

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You don't have the required permission to use this command, type -perms to see the required permissions for commands")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please enter all the  required arguments to run this command, type -help for commands")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("Command not found, type -help to view commands")
    elif isinstance(error,commands.MemberNotFound):
        await ctx.send("Member not found, please recheck the argument")           
    else:
        raise error   
        

bot.loop.create_task(ch_pr())  
bot.run("<Put TOKEN Here>")    