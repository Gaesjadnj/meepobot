import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import keep_alive
from keep_alive import keep_alive
import datetime
import time
import aiohttp
import os
from pyjokes import get_joke
import ast
import praw
import sys
import random
import discord.utils
import json
import youtube_dl
import danksearch
import covid
from udpy import UrbanClient
from owotext import OwO
from pkg_info import get_pkg_info
from covid import Covid
from discord import Game

danksearch.SAFESEARCH = True

client = UrbanClient()

start_time = time.time()

uwu = OwO()

covid = Covid(source="worldometers")
      
    
      
reddit = praw.Reddit(client_id='GKg9xGGzV4vM9Q', client_secret='FutzuRgQ-0-fFTlOsbbDeJPdcUg', user_agent='Eternal City Bot by u/RedPhantomIRP')

bot = commands.Bot(command_prefix="??", description="Insert-Description")

bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))

async def statuschange():
    await bot.wait_until_ready() # Makes the bot wait until it's fully ready before the stuff below are ran
    while True: # The while makes it loop the stuff below forever
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name="??help", type = discord.ActivityType.listening)) # This line makes it change status to playing
        await asyncio.sleep(5) # This line makes it waits 5 seconds
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name=f"with {len(bot.commands)} commands!", type = discord.ActivityType.playing))
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name=f"{len(bot.users)} Users! in {len(bot.guilds)} Guilds!", type = discord.ActivityType.watching)) # This line makes it change status to listening
        await asyncio.sleep(5) # Makes it wait another 5 seconds and then it'll go back to the top on playing because we used "while" which makes it look

    await statuschange() # This calls the status function that i made above
    bot.loop.create_task(statuschange()) # This in't needed but it's there to make it run in the background to avoid possible erros etc.
@bot.event
async def on_ready():
    print("change status started")
    print(discord.utils.oauth_url(bot.user.id))
    print(str(datetime.datetime.now().time()) + " - Connected to Discord API.")
    print(str(datetime.datetime.now().time()) + " - Loading stats and posting to DBL...")
    print(str(datetime.datetime.now().time()) + " - Loading complete!")
    print(str(datetime.datetime.now().time()) + " - Primed and set.")
    await statuschange()# This calls the status function that i made above
    bot.loop.create_task(statuschange())

@bot.command()
async def pendmessage(ctx, *, member: discord.Member = None):
    try:
        if member is None:
            await ctx.send(ctx.author.mention + " Error! Please define a user to set the application to pend! ")
        else:
            if member.id == ctx.author.id:
                await ctx.send(ctx.author.mention + " Error! Please define a user to set the application to pend! Not Yourself!")
            else:
                embed=discord.Embed(description="Please be patient while your application is pending. Other staff need more opinions to be accepted.")
                await ctx.send(embed=embed)
    except:
        pass



@bot.command()
async def prefix(ctx):
  await ctx.send(f"My prefix is {server_prefix}")

@bot.command()
async def endgiveawaycode(ctx, winner1, winner2):
    embed = discord.Embed(title=':tada: **Giveaway Ended** :tada:', color=ctx.author.top_role.colour)
    embed.add_field(name='Hosted By:', value=f"{ctx.author.mention} ID: [{ctx.author.id}]", inline=False)
    embed.add_field(name='Winners:', value=f"{winner1} & {winner2} (I will DM you the code in about an hour)", inline=False)
    embed.add_field(name='Date Recorded:', value=ctx.message.created_at.strftime("%A, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.set_footer(text='Better luck next time yall!')
    await ctx.send(embed=embed)
    channel = discord.utils.get(ctx.guild.channels, name="giveaway-logs")
    embed = discord.Embed(title="", description=f"{ctx.author.mention} ended the giveaway in {ctx.channel.mention}!")
    embed.add_field(name=f'Winners', value=f'{winner1} & {winner2}', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await channel.send(embed=embed)

@bot.command()
async def endgiveaway(ctx, *, reason=None):
    embed = discord.Embed(title=':tada: **Giveaway Ended** :tada:', color=ctx.author.top_role.colour)
    embed.add_field(name='Hosted By:', value=f"{ctx.author.mention} ID: [{ctx.author.id}]", inline=False)
    embed.add_field(name='Winners:', value=f"{reason}", inline=False)
    embed.add_field(name='Date Recorded:', value=datetime.datetime.now(), inline=False)
    embed.set_footer(text='Better luck next time yall!')
    await ctx.send(embed=embed)






@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)
    embed = discord.Embed(title=f"{ctx.author},", description=f"Added role `{role.name}` to {user.mention}")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.remove_roles(role)
    embed = discord.Embed(title=f"{ctx.author},", description=f"Removed role `{role.name}` from {user.mention}")
    await ctx.send(embed=embed)








@bot.command()
async def userinfo(ctx, member : discord.Member=None):
    if member is None:
      await ctx.send('`INVALID` Usage. Use `??userinfo @ExampleUser#1992` Instead`')
    else:
        roles = [role for role in member.roles]

        embed = discord.Embed(title="User Information", colour=member.color, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.display_name, icon_url=member.avatar_url)
        embed.set_footer(text="Requested by: {}".format(ctx.author), icon_url=ctx.author.avatar_url)

        embed.add_field(name="**:ideograph_advantage: Discord Tag**", value=member, inline=False)
        embed.add_field(name="**:pencil2: Nickname**", value=member.nick, inline=False)
        embed.add_field(name="**:video_game: Game/Activity**", value=member.activity, inline=False)
        embed.add_field(name="**:woman_mechanic: Has Animated PFP?**", value=member.is_avatar_animated())
        embed.add_field(name="**:id: User ID**", value=member.id, inline=False)
        embed.add_field(name="**:robot: is Bot?**", value=member.bot, inline=False)
        embed.add_field(name=f"**<:3670_NitroBoost:725609607010975754> Boosting {ctx.guild.name} Since**", value=member.premium_since, inline=False)
        embed.add_field(name="**:busts_in_silhouette: Joined Discord at**", value=member.created_at.strftime("%A, %B %d %Y %H:%M %p"))
        embed.add_field(name="**:speech_left: Joined Server**", value=member.joined_at.strftime("%A, %B %d %Y %H:%M%p"))
        embed.add_field(name="**Currently In Server**", value=f"{ctx.author.guild} | Owner: **{ctx.guild.owner}**", inline=False)
        embed.add_field(name="**:red_circle: Current Status**", value=member.status, inline=False)
        embed.add_field(name="**:scroll: Top Role**", value=member.top_role, inline=False)
        embed.add_field(name="**:scroll: Roles**", value=''.join([role.mention for role in roles]))
            
        await ctx.send(embed=embed)

@bot.command()
async def cinfo(ctx, channel):
    embed = discord.Embed(title="Channel Information", description="")
    embed.add_field(name="Name", value=f"{ctx.channel.name}", inline=False)
    embed.add_field(name="ID", value=ctx.channel.id, inline=False)
    embed.add_field(name="Topic", value=ctx.channel.topic, inline=False)
    embed.add_field(name="NSFW?", value=ctx.channel.is_nsfw(), inline=False)
    embed.add_field(name="Category", value=ctx.channel.category, inline=False)
    embed.add_field(name="Position", value=ctx.channel.position, inline=False)
    embed.add_field(name="Channel Created At", value=ctx.channel.created_at.strftime("%A, %B %d %Y %H:%M%p"), inline=False)
    embed.add_field(name="Slowmode", value=f"{ctx.channel.slowmode_delay} Second(s)", inline=False)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.event
async def on_member_update(before, after):
  channel = discord.utils.get(before.guild.text_channels, name="logs-reports")
  roles = [role for role in before.roles]
  roless = [role for role in after.roles]

  if before.roles != after.roles:
    embed = discord.Embed(color=before.colour, description=f"{before}'s Roles Change")
    embed.set_author(name=f"{before} ({before.id})", icon_url=before.avatar_url)
    embed.add_field(name=f"**Before:** ( {len(before.roles)} ) :", value=" ".join([role.mention for role in roles]))
    embed.add_field(name=f"**After:** ( {len(after.roles)} ) :", value=" ".join([role.mention for role in roless]))
    embed.set_footer(text=f"{datetime.datetime.now()}")
    await channel.send(embed=embed)  
  elif channel is None:
    return  
  else:
    return

    
@bot.command()
async def createticket(ctx, member : discord.Member, *, reason=None):
  bot.wait_until_ready()
  c = bot.get_channel(680745011037470802)
  if reason is None:
    embed = discord.Embed(title=':x: **Invalid Ticket**', color=ctx.author.top_role.colour)
    embed.add_field(name='Argument:', value=f"The user that created this ticket did not state a message, therefor the ticket was denied.", inline=False)
    embed.add_field(name='Ticket Created By:', value=f"**{ctx.author}**", inline=True)
    embed.add_field(name='User ID:', value=f"{ctx.author.id}")
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(title=':warning: **NEW TICKET**', color=ctx.author.top_role.colour)
    embed.add_field(name='play.enchantedpvp.com', value=f"", inline=True)
    embed.add_field(name='Ticket Owner:', value=f"**{ctx.author}**", inline=True)
    embed.add_field(name='Issue/Concern:', value=f"{reason}", inline=False)
    embed.add_field(name='User ID:', value=f"{ctx.author.id}")
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def threechoice(ctx, *, reason=None):
    msg = await ctx.send(f"{reason}")
    await msg.add_reaction("<:CheckMark:586503709853220864>")
    await msg.add_reaction("<:6699_none:702035629701070869>")
    await msg.add_reaction("<:7685_no:702036295534379098>")


@bot.command()
@commands.is_owner()
async def embed(ctx, *, message):
 for guild in bot.guilds:
  for channel in guild.channels:
    if channel.name == "steveo-zone":
      try:
        await channel.send(message, embed=embed)
        print(f"{guild} got the changelog.")
      except:
          print(f"{guild} didn't get the changelog.")
print("Action Completed.")

@bot.command(pass_context=True)
async def yesorno(ctx, *, reason=None):
    msg = await ctx.send(f"{reason}")
    await msg.add_reaction("<:6940_agree:702035143472447548>")
    await msg.add_reaction("<:1665_disagree:702035123541114921>")


@bot.command(pass_context=True)
async def choose(ctx, *choices : str):
   embed=discord.Embed(title="Random Choice Generator", description="The Choice Has been Made", color=0x176cd5)
   embed.add_field(name="Choices", value=choices, inline=False)
   embed.add_field(name="The Decision has been made. I choose", value=random.choice(choices), inline=False)
   embed.set_thumbnail(url='https://h5p.org/sites/default/files/styles/medium-logo/public/logos/multichoice-icon_0.png?itok=2unJ_RVE')
   await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def slots(ctx):
    responces = [":watermelon:",":kiwi:",":cherries:"]
    embed=discord.Embed(title="Slot Machine")
    embed.add_field(name="Roll 1", value=random.choice(responces) + random.choice(responces) + random.choice(responces), inline=False)
    embed.add_field(name="Roll 2", value=random.choice(responces) + random.choice(responces) + random.choice(responces), inline=False)
    embed.add_field(name="Roll 3", value=random.choice(responces) + random.choice(responces) + random.choice(responces), inline=False)
    embed.set_thumbnail(url='https://image.flaticon.com/icons/png/512/247/247845.png')
    embed.set_footer(text="Play to your own risk")
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def setnick(ctx, user: discord.Member, *, name):
  await user.edit(nick=name)
  await ctx.send(f"<:3495_YesOVE:574158597370675211> You changed {user.name}(s) nick to **{name}**")

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member=None):
    if not user:
        user = ctx.author
    embed = discord.Embed(title=f"{user.name}'s Avatar", color=0x176cd5, timestamp=ctx.message.created_at)
    embed.set_image(url=user.avatar_url)
    embed.set_author(name=user, icon_url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def makemeabot(ctx, *, reason=None):
  bot.wait_until_ready()
  c = bot.get_channel(702354197919694859)
  if reason is None:
    embed = discord.Embed(title='**Invalid MMAB Ticket**', color=ctx.author.top_role.colour)
    embed.add_field(name='Written By:', value=f"**{ctx.author.mention}**", inline=True)
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(title='<:3224_info:701081464623726702> **NEW: MAKEMEABOT TICKET**', color=ctx.author.top_role.colour)
    embed.add_field(name='User:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='What They Want:', value=f"{reason}", inline=False)
    embed.add_field(name='User ID:', value=f"{ctx.author.id}", inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=datetime.datetime.now())
    await ctx.message.delete()
    await ctx.send('<:3495_YesOVE:574158597370675211> **Success**, Your MakeMeABot ticket was submitted. Please be patient and wait for a reply.')
    await c.send(embed=embed)

@bot.command(aliases=["list", "list-roles", "show", "display", "listroles"])
async def listrole(self, ctx):
        result = config.guildscol.find_one({"guild": ctx.guild.id})
        currentRoles = []
        for roleID in result["staffRoles"]:
            try:
                currentRoles.append(discord.utils.get(ctx.guild.roles, id=roleID).name)
            except Exception:
                pass
        currentRoles = "`, `".join(currentRoles)
        if currentRoles == "":
            currentRoles = f"No staff roles on this server. Add some with {ctx.prefix}staff-role add `<@role | role>`!"
        embed = discord.Embed(title=f"{ctx.guild.name} staff roles:", description=f"`{currentRoles}`", colour=0x00988E,
                              timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, time: int = None):
   if time == None:
     embed = discord.Embed(title="Slowmode Usage", description="Slowmode: Enable a 'Chat Cooldown' to slow down your chat.\n\nUse: ??slowmode 1-21600")
     await ctx.send(embed=embed)
   if time == 0:
     await ctx.channel.edit(slowmode_delay=0)
     embed = discord.Embed(title=f"{ctx.author},", description=f"<:2894_DontOve:574158582417719326> Turned `OFF` Slowmode")
     await ctx.send(embed=embed)
   else:
     await ctx.channel.edit(slowmode_delay=time)
     embed = discord.Embed(title=f"{ctx.author},", description=f"<:3495_YesOVE:574158597370675211> Turned Slowmode `ON` to **{time}(s)**")
     await ctx.send(embed=embed)


@bot.command()
async def help(ctx, arg=None):
  if arg == None:
    embed = discord.Embed(title=f"Hello {ctx.author.name}! Here's a list of my current categorys!", colour=0x176cd5, url='https://google.com/')
    embed.add_field(name='<:5695_staffbot:573416328090746880> **Moderation**', value=f"Type `??help moderation` to view the commands.", inline=False)
    embed.add_field(name='<:2297_spin_gear:573418663097663488> **Utility**', value=f"Type `??help utility` to view the commands.", inline=True)
    embed.add_field(name='<:5488_OveEyesOFF:574158618669350912> **Fun**', value=f"Type `??help fun` to view the commands.", inline=False)
    embed.add_field(name='<:9375_Information:712829268589150208> **Support**', value=f"Type `??help support` to view the commands.", inline=False)
    embed.add_field(name='<:3235_warning2:713021817299796029> **Stats**', value=f"Type `??help stats` to view the commands.", inline=False)
    embed.add_field(name='🎉 **Giveaways**', value=f"Type `??help giveaways` to view the commands.", inline=False)
    embed.add_field(name='Links:', value="[Support Server](https://discord.gg/NYVEZTH)\n[Invite Me](https://discordapp.com/oauth2/authorize?client_id=680674076905177119&scope=bot)", inline=False)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M GMT"))
    await ctx.send(embed=embed)
  elif arg == "utility":
    embed = discord.Embed(title=f"Current Utility Commands", colour=0x176cd5, timestamp=ctx.message.created_at)
    embed.add_field(name='**??slowmode (0 Seconds - 6000 Seconds)**', value=f"```Enables discordSlowmode in the selected channel, durationTimeout.```", inline=False)
    embed.add_field(name="**??joined (User,UserID)**", value="```Gives a return on when the user joined the guild.```", inline=True)
    embed.add_field(name='**??setnick (User,UserID) (Set-Nickname)**', value=f"```Change the current nickname of that user.```", inline=False)
    embed.add_field(name='**??yesorno (question)**', value=f"```Create a miniPoll with a yes or no reaction.```", inline=True)
    embed.add_field(name='**??poll (question)**', value="```Create a Poll with three reactions, 1,2,3.```")
    embed.add_field(name='**??threechoice (question)**', value="```Create a miniPoll with three reactions, tick,middle,no.```", inline=True)
    embed.add_field(name='**??serverinfo**', value="```Shows detailed information about the guild your in.```", inline=True)
    embed.add_field(name='**??userinfo (User,UserID)**', value="```Shows detailed information about the user mentioned.```", inline=True)
    embed.add_field(name='**??avatar (User,UserID)**', value="```Preview the bot/user's avatar.```", inline=True)
    embed.add_field(name='**??ping**', value="```Shows the current bot latency.```", inline=True)
    embed.add_field(name='**??addrole (User,UserID) (RoleName)**', value="```Gives the selected roles to the user.```", inline=True)
    embed.add_field(name='**??removerole (User,UserID) (RoleName)**', value="```Removes the selected role from that user.```", inline=True)
    embed.add_field(name='**??say (message)**', value="```Returns your text, but from the bot.```", inline=True)
    embed.add_field(name='**??servericon**', value="```Preview the server icon.```", inline=True)
    embed.add_field(name='**??createchannel (channelName)**', value="```Creates a new channel with the name you provided.```", inline=True)
    embed.add_field(name='**??deletechannel (channelName)**', value="```Deletes the channel with the name you provided.```", inline=True)
    embed.add_field(name='**??cinfo**', value="```Shows information about that channel.```", inline=True)
    embed.add_field(name='**??shout (message)**', value="```Shouts a message.```", inline=True)
    embed.add_field(name='**??announce (message)**', value="```Announces a message in your server.```", inline=True)
    embed.add_field(name='**??setup**', value="```Sets up all the needed channels for you to get Meepo's latest updates!```", inline=True)
    embed.add_field(name='**??pypi (package)**', value="```Finds a python package with the name you provided.```", inline=True)
    embed.set_author(name='Meepo - Utility Help (21 Commands)')
    embed.set_footer(text=f'Meepo')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  elif arg == "moderation":
    embed = discord.Embed(title=f"Current Moderation Commands", colour=0x176cd5, timestamp=ctx.message.created_at)
    embed.add_field(name='**??ban (User,UserID) (banReason)**', value="```Removes that user from the server.```", inline=True)
    embed.add_field(name='**??kick (User,UserID) (kickReason)**', value="```Kicks that user from the server.```", inline=True)
    embed.add_field(name='**??warnuser (User,UserID) (warnReason)**', value="```Warns that user by sending them a DM.```", inline=True)
    embed.add_field(name="**??mute (User,UserID)**", value="```Mutes the user specified (Need role Muted).```", inline=True)
    embed.add_field(name="**??unmute (User,UserID)**", value="```Removes the Muted role from the user.```", inline=True)
    embed.add_field(name="**??history user/global**", value="```WIP... View mute/ban/warn offences globally, or from a specific user.```")
    embed.add_field(name="**??purge (messages)", value="```Purges the amount of messsages from the chat.```", inline=True)
    embed.set_footer(text='Meepo')
    embed.set_author(name='Meepo - Moderation Help (7 Commands)')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  elif arg == "fun":
    embed = discord.Embed(title=f"Current Fun Commands", colour=0x176cd5, timestamp=ctx.message.created_at)
    embed.add_field(name='**??punch (User)**', value="```Gives that user a hard punch! :3```", inline=False)
    embed.add_field(name='**??slap (User)**', value="```Slaps that user on the face! :3```", inline=False)
    embed.add_field(name='**??shoot (User)**', value="```Shoots that user! ¯\_(ツ)_/¯```", inline=False)
    embed.add_field(name='**??hug (User)**', value="```Gives the user a random hug!```", inline=False)
    embed.add_field(name='**??slots**', value="```Rolls the slot machine!```", inline=False)
    embed.add_field(name='**??choose <arg-1> <arg-2> <arg-3>**', value="```Makes the bot choose a random choice.```", inline=False)
    embed.add_field(name='**??meme**', value="```Shows a random reddit meme!```", inline=False)
    embed.add_field(name='**??dankmeme**', value="```Shows a random dankMeme!```", inline=True)
    embed.add_field(name='**??joke**', value="```Shows a VERY bad joke :3```", inline=False)
    embed.add_field(name='**??add (number-1) (number-2)**', value="```Adds the two numbers together```", inline=False)
    embed.add_field(name='**??8ball (question)**', value="```What may the magic 8ball say!```", inline=False)
    embed.add_field(name="**??search (query)**", value="```Search up a Query on youtube!```", inline=False)
    embed.add_field(name="**??google <query>**", value="```Search up a Query on Google.com!```", inline=False)
    embed.add_field(name="**??spoil (text)**", value="```Puts the text in a spoiler ;/```", inline=False)
    embed.add_field(name='**??L (User,UserID)**', value=f"```Give the user a PHAT L```", inline=False)
    embed.add_field(name='**??cookie**', value=f"```Give the user a yummy cookie to eat!```", inline=False)
    embed.add_field(name="**??setprofile**", value="```Start to set up a imaginary character for your profile!```", inline=False)
    embed.add_field(name="**??profile**", value="```Preview your character!```")
    embed.add_field(name="**??winner (messageID) (giveawayWinners)**", value="```Selects (user)s randomly from the giveaway.```")
    embed.set_author(name='Meepo - Fun Help (19 Commands)')
    embed.set_footer(text='Meepo')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
  elif arg == "giveaway":
    embed = discord.Embed(title="", description="**Meepo Giveaways**", color=0x176cd5)
    embed.add_field(name='**Information:**', value="Start a **Giveaway** that people can enter. You can put set time and date for the givaways.\n\n**Normal Giveaway Command/Example:**\n```??startgiveaway <days> <winners> <date-finishing> <prize/description>```\n**Example:**\n```??startgiveaway 7 2 30/03/2020 x2 Game Keys```\n\n\n**Ping Giveaway Command/Example:**\n```??startgiveawayping <days> <winners> <date-finishing> <prize/description>```\n**Example:**\n```??startgiveawayping 1 5 28/06/2019 x5 Game Keys```\n\n**[!] Friendly Reminder:** In order to make the giveaway ping work you must have a role name '@Giveaways' (CaSe SeNSiTiVE)\n**IMPORTANT:** Currently, The Startgiveawayping command does not work.", inline=False)
    await ctx.send(embed=embed)
  elif arg == "giveaways":
    embed = discord.Embed(title="Meepo - Giveaway Module :tada:", description="", color=0x176cd5)
    embed.add_field(name='**Information:**', value="Start a **Giveaway** that people can enter. You can put set time and date for the givaways.\n\n**Normal Giveaway Command/Example:**\n```??startgiveaway <days> <winners> <date-finishing> <prize/description>```\n**Example:**\n```??startgiveaway 7 2 30/03/2020 x2 Game Keys```\n\n\n**Ping Giveaway Command/Example:**\n```??startgiveawayping <days> <winners> <date-finishing> <prize/description>```\n**Example:**\n```??startgiveawayping 1 5 28/06/2019 x5 Game Keys```\n\n**[!] Friendly Reminder:** In order to make the giveaway ping work you must have a role name 'Giveaways' (CaSe SeNSiTiVE)\n**IMPORTANT:** Currently, The Startgiveawayping command does not work", inline=False)
    await ctx.send(embed=embed)
  elif arg == "support":
    embed = discord.Embed(title="Current Support Modules", description=f"Last Updated: Friday 15th May, 2:06PM")
    embed.add_field(name="**Bot Issue Thread Report**", value="If at ANYTIME of the bot/commands not working please make a thread with this command `??reportissue {whats not working}` and i will try to fix it **ASAP**. Please also do not spam the bot issue threads as it will end up in you being blacklisted from using that command. :warning:")
    embed.add_field(name="**Report A User**", value="If you find a user exploiting/abusing 'Meepo' Please make a user report thread using command `??reportuser {user} {explaination}` with screenshot evidence, that user will be dealt with.")
    await ctx.send(embed=embed)
  elif arg == "search":
    await ctx.send(f'<:HiAppHere_com_com:712829285706235948> - **This command has not been added yet.**')  
  elif arg == "stats":
    embed = discord.Embed(title="Stat/Worldwide Info", description=f"Last Updated: Thursday 21st May, 11:25PM")
    embed.add_field(name="**??covid**", value="Shows the worldwide COVID-19 Stats.", inline=False)
    embed.add_field(name="**??bitcoin**", value="Shows the current value of the bitcoin.", inline=False)
    embed.set_footer(text='Rewrite In Progress.')
    embed.set_author(name='Stats Info (2 Commands)')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def startgiveaway(ctx, day, win, date, *, reason):
    await ctx.message.delete() 
    embed = discord.Embed(title=':tada: **Giveaway Time** <:7499_HypeGhost:725609706344808460>', color=ctx.author.top_role.colour, timestamp=ctx.message.created_at)
    embed.add_field(name='Hosting:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='Duration:', value=f"**{day}** Day(s)", inline=True)
    embed.add_field(name='Winners:', value=f"**{win}** ", inline=True)
    embed.add_field(name='Date Stated:', value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.add_field(name='Date Ending:', value=f"{date}", inline=False)
    embed.add_field(name='Description:', value=f"{reason}", inline=False)
    embed.add_field(name='Requirement To Enter:', value="React With <:4214_notify:725609620621754370> to enter!", inline=False)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=f"GA: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("<:4214_notify:725609620621754370>")
    channel = discord.utils.get(ctx.guild.channels, name="giveaway-logs")
    embed = discord.Embed(title="", description=f"**Log for giveaway started in {ctx.channel.mention}**")
    embed.add_field(name=f'Hosting:', value=f'{ctx.author.mention} [{ctx.author}]', inline=False)
    embed.add_field(name=f'ID:', value=f'{ctx.author.id}', inline=False)
    embed.add_field(name=f'Server Hosted From:', value=f'{ctx.guild.name}', inline=False)
    embed.add_field(name=f'Winners:', value=f'{win}', inline=False)
    embed.add_field(name=f'Day(s):', value=f'{day}', inline=False)
    embed.add_field(name=f'Date Started:', value=f'{ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC")}', inline=False)
    embed.add_field(name=f'Date Ending:', value=f'{date}', inline=False)
    embed.add_field(name=f'Description:', value=f'{reason}', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await channel.send(embed=embed)
@bot.command()
@commands.has_permissions(manage_messages=True)
async def winner(ctx, msg, winnerss: int=1):
    msg=await ctx.channel.fetch_message(int(msg))
    if msg:

        data=[reaction for reaction in msg.reactions if str(reaction.emoji)=="<:4214_notify:725609620621754370>"]
        if len(data)==0:
          return 
        users=[]
        async for user in data[0].users():
            if not user.bot:
                users.append(user)
        winners=[]
        for i in range(winnerss):
            winner=random.choice(users)
            winners.append(winner.mention)
            users.pop(users.index(winner))
        embed = discord.Embed(title=":tada: Giveaway ended :tada:", color=ctx.author.top_role.colour)
        embed.add_field(name="Hosted By:", value=f"{ctx.author.mention} ID: [{ctx.author.id}]", inline=False)
        embed.add_field(name="Winners:", value=f"{','.join(winners)}", inline=False)
        embed.add_field(name="Date Recorded:", value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def urlg(ctx, day, win, date, link, *, reason):
    await ctx.message.delete() 
    embed = discord.Embed(title=':tada: **Giveaway Active** <:5488_OveEyesOFF:574158618669350912>', color=ctx.author.top_role.colour, timestamp=ctx.message.created_at)
    embed.add_field(name='Hosting:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='Duration:', value=f"**{day}** Day(s)", inline=True)
    embed.add_field(name='Winners:', value=f"**{win}** ", inline=True)
    embed.add_field(name='Date Stated:', value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.add_field(name='Date Ending:', value=f"{date}", inline=False)
    embed.add_field(name='Link To Enter:', value=f"{link}", inline=False)
    embed.add_field(name='Description:', value=f"{reason}", inline=False)
    embed.add_field(name='Requirement To Win:', value="React With <:1641_Sino:702079170510848011>   to enter!", inline=False)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=f"GA: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    msg = await ctx.send(embed=embed)
    await ctx.send(f"{link}")
    await msg.add_reaction("<:1641_Sino:702079170510848011>")
    channel = discord.utils.get(ctx.guild.channels, name="giveaway-logs")
    embed = discord.Embed(title="", description=f"**Log for giveaway started in {ctx.channel.mention}**")
    embed.add_field(name=f'Hosting:', value=f'{ctx.author.mention} [{ctx.author}]', inline=False)
    embed.add_field(name=f'ID:', value=f'{ctx.author.id}', inline=False)
    embed.add_field(name=f'Server Hosted From:', value=f'{ctx.guild.name}', inline=False)
    embed.add_field(name=f'Winners:', value=f'{win}', inline=False)
    embed.add_field(name=f'Day(s):', value=f'{day}', inline=False)
    embed.add_field(name=f'Date Started:', value=f'{ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC")}', inline=False)
    embed.add_field(name=f'Date Ending:', value=f'{date}', inline=False)
    embed.add_field(name=f'Description:', value=f'{reason}', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await channel.send(embed=embed)
@bot.command()
@commands.has_permissions(manage_messages=True)
async def gwinner(ctx, msg, winnerss: int=1):
    msg=await ctx.channel.fetch_message(int(msg))
    if msg:

        data=[reaction for reaction in msg.reactions if str(reaction.emoji)=="<:1641_Sino:702079170510848011>"]
        if len(data)==0:
          return 
        users=[]
        async for user in data[0].users():
            if not user.bot:
                users.append(user)
        winners=[]
        for i in range(winnerss):
            winner=random.choice(users)
            winners.append(winner.mention)
            users.pop(users.index(winner))
        embed = discord.Embed(title=":tada: Giveaway ended :tada:", color=ctx.author.top_role.colour)
        embed.add_field(name="Hosted By:", value=f"{ctx.author.mention} ID: [{ctx.author.id}]", inline=False)
        embed.add_field(name="Winners:", value=f"{','.join(winners)}", inline=False)
        embed.add_field(name="Date Recorded:", value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
        await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def downtime(ctx, *, message):
 for guild in bot.guilds:
  for channel in guild.channels:
    if channel.name == "general":
      try:
        await channel.send(message)
        print(f"{guild} got the changelog.")
      except:
          print(f"{guild} didn't get the changelog.")
print("Action Completed.")


@bot.command()
async def startgiveawayping(ctx, day, win, date, *, reason):
    await ctx.message.delete() 
    embed = discord.Embed(title=':tada: **Giveaway Active** <:5488_OveEyesOFF:574158618669350912>', color=ctx.author.top_role.colour, timestamp=ctx.message.created_at)
    embed.add_field(name='Hosting:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='Duration:', value=f"**{day}** Day(s)", inline=True)
    embed.add_field(name='Winners:', value=f"**{win}** ", inline=True)
    embed.add_field(name='Date Stated:', value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.add_field(name='Date Ending:', value=f"{date}", inline=False)
    embed.add_field(name='Description:', value=f"{reason}", inline=False)
    embed.add_field(name='Requirement To Enter:', value="React With <:1641_Sino:702079170510848011>   to enter!", inline=False)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=f"GA: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    msg = await ctx.send(embed=embed)
    role = discord.utils.get(ctx.guild.roles, name="Giveaways")
    await ctx.send(role.mention)
    await msg.add_reaction("<:1641_Sino:702079170510848011>")
    channel = discord.utils.get(ctx.guild.channels, name="giveaway-logs")
    embed = discord.Embed(title="", description=f"**Log for giveaway started in {ctx.channel.mention}**")
    embed.add_field(name=f'Hosting:', value=f'{ctx.author.mention} [{ctx.author}]', inline=False)
    embed.add_field(name=f'ID:', value=f'{ctx.author.id}', inline=False)
    embed.add_field(name=f'Server Hosted From:', value=f'{ctx.guild.name}', inline=False)
    embed.add_field(name=f'Winners:', value=f'{win}', inline=False)
    embed.add_field(name=f'Day(s):', value=f'{day}', inline=False)
    embed.add_field(name=f'Date Started:', value=f'{ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC")}', inline=False)
    embed.add_field(name=f'Date Ending:', value=f'{date}', inline=False)
    embed.add_field(name=f'Description:', value=f'{reason}', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def channel(ctx, type = None, *, name = None, name2 = None):
  channel = discord.utils.get(ctx.guild.channels, name="logs-reports")
  if channel == None:
    await ctx.send("Please run the setup by using `d/setup`.")
  else:
    xyz = discord.utils.get(ctx.guild.channels, name=name)
    if type == "lock":
      if name == None:
        error = discord.Embed(title=":x: Invalid argument", description="**d/channel lock <channel name>**", color = discord.Colour.red())
        await ctx.send(embed=error)
      else:
        overwrite = discord.PermissionOverwrite(send_messages=False)
        embed = discord.Embed(description=f":white_check_mark: {xyz} locked.", color = discord.Colour.green())
        embed2 = discord.Embed(description=":white_check_mark: Channel locked.", color = discord.Colour.green())
        logchannel = discord.utils.get(ctx.guild.channels, name="donut-logs")
        log = discord.Embed(description=f"Used `channel` command in {ctx.channel}\nd/channel lock {name}", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
        log.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        await xyz.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(embed=embed)
        await xyz.send(embed=embed2)
        await logchannel.send(embed=log)
    elif type == "unlock":
      if name == None:
        error = discord.Embed(title=":x: Invalid argument", description="**d/channel unlock <channel name>**", color = discord.Colour.red())
        await ctx.send(embed=error)
      else:
        overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True)
        embedunlock = discord.Embed(description=f":white_check_mark: {xyz} unlocked.", color = discord.Colour.green())
        embedunlock2 = discord.Embed(description=":white_check_mark: Channel unlocked.", color = discord.Colour.green())
        logchannel = discord.utils.get(ctx.guild.channels, name="donut-logs")
        log = discord.Embed(description=f"Used `channel` command in {ctx.channel}\nd/channel unlock {name}", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
        log.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        await xyz.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(embed=embedunlock)
        await xyz.send(embed=embedunlock2)
        await logchannel.send(embed=log)
    elif type == "slowmode":
      logchannel = discord.utils.get(ctx.guild.channels, name="donut-logs")
      log = discord.Embed(description=f"Used `channel` command in {ctx.channel}\nd/channel slowmode {name}", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
      log.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
      if name == None:
        error = discord.Embed(color = discord.Colour.red(), title=":x: Invalid argument", description="**d/channel slowmode <time>**")
        await ctx.send(embed=error)
      elif name == "0":
        await ctx.channel.edit(slowmode_delay=name)
        embed = discord.Embed(description=":white_check_mark: Turned off slowmode.", color = discord.Colour.green())
        await ctx.send(embed=embed)
        await logchannel.send(embed=log)
      else:
        await ctx.channel.edit(slowmode_delay=name)
        embed = discord.Embed(description=f":white_check_mark: Slowmode was set to {name} seconds.", color = discord.Colour.green())
        await ctx.send(embed=embed)
        await logchannel.send(embed=log)
    else:
      embed = discord.Embed(title="Command: ??channel", description="`??channel lock <channel name>`\n`??channel unlock <channel name>`\n`??channel slowmode <time>`", color = discord.Colour.blue())
      await ctx.send(embed=embed)

@bot.command(name="m-unlock")
@commands.has_permissions(administrator=True)
async def munlock(ctx, type = None, *, name = None):
    channel = discord.utils.get(ctx.guild.channels, name="logs-reports")
    if channel == None:
        await ctx.send("Please run the setup by using `<prefix>setup`.")
    else:
        if type == "1":
            embed = discord.Embed(title="Maintenance Mode • Unlock 1", color = discord.Colour.red(), description="Unlocking all channels..", timestamp=ctx.message.created_at)
            test = await ctx.send(embed=embed)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            for channel in ctx.guild.channels:
                try:
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                except:
                    pass
            xyz = discord.Embed(title="Maintenance Mode • Unlocked", description=f"Maintenance mode disabled.", color=discord.Colour.green(), timestamp=ctx.message.created_at)
            await test.edit(embed=xyz)
            woi = discord.utils.get(ctx.guild.channels, name="maintenance-mode")
            await woi.delete()
            log = discord.Embed(description=f"Used `m-unlock` command in {ctx.channel.mention}\nd/m-unlock 1", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
            log.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            channel = discord.utils.get(ctx.guild.channels, name="donut-logs")
            await channel.send(embed=log)
        elif type == "2":
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            overwrite.read_messages = True
            XYZ = discord.utils.get(ctx.guild.channels, name=name)
            if name == None:
                embed = discord.Embed(title=":x: Invalid argument", description=f"**d/m-unlock 2 <channel name>**", color = discord.Colour.red())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Maintenance Mode • Unlock 2", color = discord.Colour.red(), description=f"Unlocking channel..", timestamp=ctx.message.created_at)
                test = await ctx.send(embed=embed)
                await XYZ.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                embeds = discord.Embed(title="Maintenance Mode • Unlocked", color = discord.Colour.green(), description=f"{XYZ.mention} has been unlocked.", timestamp=ctx.message.created_at)
                await test.edit(embed=embeds)
                woi = discord.utils.get(ctx.guild.channels, name = "donut-logs")
                log = discord.Embed(description=f"Used `m-unlock` command in {ctx.channel.mention}\nd/m-unlock 2 {name}", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
                log.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                await woi.send(embed=log)
        elif type == "3":
            if name == None:
                embederror = discord.Embed(title=":x: Invalid argument", color = discord.Colour.red(), description="**d/m-unlock 3 <category name>**", timestamp=ctx.message.created_at)
                await ctx.send(embed=embederror)
            else:
                embedunlock = discord.Embed(title="Maintenance Mode • Unlock 3", color = discord.Colour.red(), timestamp=ctx.message.created_at, description="Unlocking category..")
                test = await ctx.send(embed=embedunlock)
                xyz = discord.utils.get(ctx.guild.categories, name=name)
                overwrite = discord.PermissionOverwrite(send_messages=True, read_messages=True)
                for channel in xyz.channels:
                    try:
                        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    except:
                        pass
                embedunlock2 = discord.Embed(title="Maintenance Mode • Unlocked", color = discord.Colour.green(), timestamp=ctx.message.created_at, description=f"Category {name} has been unlocked.")
                await test.edit(embed = embedunlock2)
                woi = discord.utils.get(ctx.guild.channels, name="donut-logs")
                log = discord.Embed(description=f"Used `m-unlock` command in {ctx.channel.mention}\nd/m-unlock 3 {name}", timestamp=ctx.message.created_at, color = discord.Colour.blue())
                log.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                await woi.send(embed=log)
        else:
            embed = discord.Embed(color=discord.Colour.blue(), timestamp=ctx.message.created_at, title="Command: d/m-unlock", description="[1] Unlock All Channels\n`d/m-unlock 1`\n\n[2] Unlock Via Channel\n`d/m-unlock 2 <channel name>`\n\n[3] Unlock Via Category\n`d/m-unlock 3 <category name>`")
            await ctx.send(embed=embed)
@munlock.error
async def munlock_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(error)
 
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Displays server information."""
    embed = discord.Embed(title=f"```{ctx.guild.name} - {ctx.guild.member_count}```", color=0x176cd5, timestamp=ctx.message.created_at)
    embed.add_field(name="Server Created", value=ctx.guild.created_at.strftime("%A, %B %d %Y %H:%M%p"), inline=False)
    embed.add_field(name="Role Count", value=len(ctx.guild.roles), inline=False)
    embed.add_field(name="Members", value=len(ctx.guild.members), inline=False)
    embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=False)
    embed.add_field(name="Region", value=ctx.guild.region, inline=False)
    embed.add_field(name="Owner", value=f"{ctx.guild.owner.mention} [{ctx.guild.owner_id}]", inline=False)
    embed.add_field(name="Verification Level", value=ctx.guild.verification_level, inline=False)
    embed.add_field(name="Emojis", value=len(ctx.guild.emojis), inline=False)
    embed.add_field(name="Server Boosters", value=ctx.guild.premium_subscribers, inline=False)
    embed.add_field(name="Booster Count", value=f"{ctx.guild.premium_subscription_count} Boost(s)", inline=False)
    embed.add_field(name="Boosting Tier", value=f"Level {ctx.guild.premium_tier}", inline=False)
    embed.add_field(name="Server Features", value=ctx.guild.features, inline=False)
    embed.add_field(name="Animated Server Icon?", value=ctx.guild.is_icon_animated(), inline=False)
    embed.add_field(name="Emoji Limit", value=ctx.guild.emoji_limit, inline=False)
    embed.add_field(name="Bitrate Limit", value=ctx.guild.bitrate_limit, inline=False)
    embed.add_field(name="Filesize Limit", value=ctx.guild.filesize_limit, inline=False)
    embed.add_field(name="Large Server?", value=ctx.guild.large, inline=False)
    embed.set_author(name=f"{ctx.guild.name} - ({ctx.guild.id})", icon_url=ctx.guild.icon_url)
    embed.set_footer(text="Made by Steveo#0068")
    await ctx.send(embed=embed)

@bot.command()
async def reload_cogs(ctx):
   await ctx.send('Reloaded giveaways')
   await asyncio.sleep(1)
   await ctx.send('Reloaded info')
   await asyncio.sleep(2)
   await ctx.send('Reloaded fun')
   await asyncio.sleep(1)
   await ctx.send('Reloaded blacklist')
   await ctx.send('`Done!`')

@bot.command(pass_context=True, name='8ball', aliases=['eightball'])
async def _8ball(ctx, *, question):
    responses = ["That is a resounding no" , "It is not looking likely", "Too hard to tell", "It is quite possible", "Definitely", "Reply hazy, try again"]
    embed=discord.Embed(title="8-Ball", color=0x176cd5)
    embed.add_field(name="**Question**", value=question, inline=False)
    embed.add_field(name="**Answer**", value=random.choice(responses), inline=False)
    embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/NrabNVYEyTdm3xThTbMnu50zMyPJcJAerVQPbbC2L1o/%3F1417132124/https/cdn.emojidex.com/emoji/seal/8ball.png')
    embed.set_author(name='8Ball ~ What may it say today')
    embed.set_footer(text=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"))
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    embed=discord.Embed(title="You have recieved a warning.", description=f"Reason: **{reason}**\nWarned by: **{ctx.author.name}**\nTime/Date: {datetime.datetime.now()}", color=0x176cd5)
    embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/26a0.png")
    await member.send(embed=embed)
    embed=discord.Embed(title=":warning: Warning was successfully issued.", color=0x176cd5)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def warnuser(ctx, member: discord.Member, *, reason=None):
    embed=discord.Embed(title="You have recieved a warning.", description=f"", color=0x176cd5)
    embed.add_field(name="Warned By:", value=f"{ctx.author.mention} [**{ctx.author}**]", inline=False)
    embed.add_field(name="Reason Warned:", value=f"{reason}", inline=False)
    embed.add_field(name="Time Warned:", value=ctx.message.created_at.strftime("%A, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/26a0.png")
    await member.send(embed=embed)
    embed=discord.Embed(title="", description=f"<:314691591484866560:714390327225745499> ***{member} has been warned.***", color=0x176cd5)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://clipground.com/images/compliment-clipart-7.jpg")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Hug someone."""
    embed = discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punch someone."""
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://petersomervell.files.wordpress.com/2017/03/d5e332f12bf6e1e7ca65a4bb6db48b94_punch20clipart-hitting-someone-clipart_1254-800.png?w=624&h=398")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    """Bans a user"""
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)
        await ctx.send(f'You successfully banned {user.name}')

@bot.command()
async def meme(ctx):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title=f'{submission.title}', color=ctx.author.colour, url=submission.url)
        embed.set_image(url=submission.url)
        embed.add_field(name="Reddit r/memes", value=f"By u/{str(submission.author)}")
        all_comments = submission.comments
        embed.set_footer(text=f"Comments: {len(all_comments)}")
        await ctx.send(embed=embed)

@bot.command()
async def baselink(ctx):
   embed = discord.Embed(title="Click here for baselink!", url="https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENTID_HERE&scope=bot&permissions=YOUR_VALUE_HERE")
   embed.add_field(name="How to invite your bot correctly", value="Replace: YOUR_CLIENT_ID_HERE with: **Your discord bot client ID**\nReplace: YOUR_VALUE_HERE with: 8 = Admin | 28392 = General Perms")
   embed.set_thumbnail(url=ctx.author.avatar_url)
   await ctx.send(embed=embed)

@bot.command()
async def dankmeme(ctx):
        memes_submissions = reddit.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title=f'{submission.title}', color=ctx.author.colour, url=submission.url)
        embed.set_image(url=submission.url)
        embed.add_field(name="Reddit r/dankmemes", value=f"By u/{str(submission.author)}")
        all_comments = submission.comments
        embed.set_footer(text=f"Comments: {len(all_comments)}")
        await ctx.send(embed=embed)


@bot.command()
async def servers(ctx):
  servers = list(bot.guilds)
  embed = discord.Embed(title="", description=f"```Meepo is connected on {str(len(servers))} Guilds!```")
  embed.add_field(name="Servers:", value='\n - '.join(server.name for server in servers))
  embed.set_footer(text="Meepo - Made to excite!", icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.send(embed=embed)




@bot.command(pass_context=True)
async def servericon(ctx, user: discord.Member=None):
    if not user:
        user = ctx.author
    embed = discord.Embed(title=f"{ctx.guild.name}'s Server Icon", color=0x176cd5, timestamp=ctx.message.created_at)
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_author(name=user, icon_url=user.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def setup(ctx, arg=None):
  if arg == None:
    embed = discord.Embed(title="", description=f"{ctx.author}, You are about to create the following")
    embed.add_field(name="About to be added:", value=f"**Meepo Category**\n`#giveaway-logs`\n`#bot-logs`\n\n**Use `??setup confirm` to complete the setup {ctx.author.name}**!")
    await ctx.send(embed=embed)
  elif arg == "confirm":
    await ctx.send(f'{ctx.author.mention}, you have completed the setup')
    guild = ctx.message.guild
    category = await ctx.guild.create_category("Meepo")
    await ctx.guild.create_text_channel("giveaway-logs", category=category)
    await ctx.guild.create_text_channel("bot-logs", category=category)

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@bot.command(aliases=['eval', 'ev', 'e'])
@commands.is_owner()
async def eval_fn(ctx, *, cmd):
    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    insert_returns(body)

    env = {
        'bot': ctx.bot,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__
    }
    exec(compile(parsed, filename="<ast>", mode="exec"), env)

    result = (await eval(f"{fn_name}()", env))
    embed=discord.Embed(title="Eval:")
    embed.add_field(name="Input", value=f"```py\n{cmd}```", inline=False)
    embed.add_field(name="Output", value=f"```py\n{result}```", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def shout(ctx, *, reason):
   embed = discord.Embed(title="", description=f"{reason}")
   embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
   await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
   embed = discord.Embed(title="", description='Pong! {0}ms <:1257_SleepingOVE:574158555079245844>'.format(round(int(bot.latency * 1000))))
   await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def L(ctx, member: discord.Member):
    msg = await ctx.send(f"Take a PHAT L, {member.mention}")
    await msg.add_reaction("<:lol:715388559422390333>")

@bot.command()
async def denied(ctx, member : discord.Member):
    embed = discord.Embed(title=':x: **Application __Denied...__**', color=ctx.author.top_role.colour)
    embed.add_field(name='Denied By:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='User Denied:', value=f"{member.mention}", inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/654447372713328680/657326479738404864/CHRISTMAS.png')
    embed.set_footer(text='Better luck next time')
    await c.send(embed=embed)



@bot.command()
async def stats(ctx):
        seconds = time.time() - start_time
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        embed = discord.Embed(title="```Meepo's Stats```", description="")
        embed.add_field(name=":1234: Users", value=f"```{len(bot.users)}```", inline=False)
        embed.add_field(name=":arrow_up_small: Guilds", value=f"```{len(bot.guilds)}```", inline=False)
        embed.add_field(name="<:9395_diagramm:725609735465730088> Uptime", value=f"```{int(h)}:{int(m)}:{int(s)}```", inline=False)
        embed.add_field(name="<:5221_mycoolessdsd:701085640581840956> Bot Owner", value="```Steveo#0068```", inline=False)
        embed.add_field(name="<:1596_PeppoUnicornioV3:571601874126635029> Bot Library", value="```discord.py```")
        embed.add_field(name="<:3379_Pin:573418645313552394> Host", value="```repl.it```", inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

@bot.command()
async def owo(ctx, *, message):
    await ctx.send(f"{uwu.whatsthis(message)}")

@bot.command()
async def reportissue(ctx, *, reason=None):
  bot.wait_until_ready()
  c = bot.get_channel(710699838701961257)
  if reason is None:
    embed = discord.Embed(title='**Invalid MMAB Ticket**', color=ctx.author.top_role.colour)
    embed.add_field(name='Written By:', value=f"**{ctx.author.mention}**", inline=True)
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(title=f"{ctx.author}'s Bot Issue Report", color=ctx.author.top_role.colour)
    embed.add_field(name='User ID:', value=f"{ctx.author.id}", inline=False)
    embed.add_field(name='Issue:', value=f"{reason}", inline=False)
    embed.add_field(name='Date Submitted', value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"Server: {ctx.guild.name}")
    await ctx.message.delete()
    await ctx.send('**Success**, You successfully submitted your bot issue report to the bot owner.')
    await c.send(embed=embed)
    
    

@bot.command()
async def pend(ctx, member : discord.Member):
    embed = discord.Embed(title=':hammer_pick: **Pending Application...**', color=ctx.author.top_role.colour)
    embed.add_field(name='Put On Hold By:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='User Pending:', value=f"{member.mention}", inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/654447372713328680/657326479738404864/CHRISTMAS.png')
    embed.set_footer(text='Getting other opinions.')
    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    embed = discord.Embed(title="Done!", description=f"Your Input: {author}")
    embed.add_field(name="Answer:", value=left + right)
    await ctx.send(embed=embed)

@bot.command()
async def report(ctx, member : discord.Member, *, reason=None):
  channel = discord.utils.get(ctx.guild.channels, name="reports")
  if reason is None:
    embed = discord.Embed(title=':x: Invalid Report :x:', description="Valid Format: `??report {user} {issue}`", color=ctx.author.top_role.colour)
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(title=f"<:5236_warning_1:712829178767998998> - **{ctx.author.name}'s Report**", color=ctx.author.top_role.colour)
    embed.add_field(name='**Reported By:**', value=f"**{ctx.author}** Their ID: [{ctx.author.id}]", inline=True)
    embed.add_field(name='**Reported User:**', value=f"**{member}** Their ID: [{member.id}]", inline=False)
    embed.add_field(name='**Reason:**', value=f"{reason}", inline=False)
    embed.add_field(name='**Date Recorded:**', value=ctx.message.created_at.strftime("%A, %#d %B %Y, %I:%M UTC"))
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text='Report Successful.')
    await ctx.message.delete()
    await ctx.send('<:3495_YesOVE:574158597370675211> **Success**, Your report was successfully made. Please wait till a member of staff can deal with your report.')
    await channel.send(embed=embed)

@bot.command()
async def announce(ctx, *, reason=None):
  bot.wait_until_ready()
  if reason is None:
    embed = discord.Embed(title="Announcement", colour=ctx.author.top_role.colour, url='https://discord.com/')
    embed.add_field(name='Written By:', value=f"**{ctx.author.mention}**", inline=True)
    embed.add_field(name='Reason:', value=f"No Reason Recorded.", inline=False)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=f"{datetime.datetime.now()}")
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(title="Announcement", colour=ctx.author.top_role.colour, url='https://google.com/')
    embed.add_field(name='Comment:', value=f"{reason}", inline=False)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text="Announced by: {}".format(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def serverupdate(ctx, member : discord.Member, *, reason=None):
  bot.wait_until_ready()
  if reason is None:
    embed = discord.Embed(title='**Announcement**', color=ctx.author.top_role.colour)
    embed.add_field(name='Written By:', value=f"**{ctx.author.mention}**", inline=True)
    embed.add_field(name='Reason:', value=f"No Reason Recorded.", inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/673142707232964627/680676791878418432/server-icon.png')
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text='1/7/2020')
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(title='**Announcement** *[Server Update]*', color=ctx.author.top_role.colour)
    embed.add_field(name='Announced By:', value=f"**{ctx.author.mention}**", inline=True)
    embed.add_field(name='Reason:', value=f"{reason}", inline=False)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/668825181707436062/680735845111562267/server-icon.png')
    embed.set_footer(text='play.enchantedpvp.com')
    await ctx.send(embed=embed)

@bot.command()
async def banlist(ctx):
   await ctx.send("There are too many banned users in this guild.")

@bot.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.mention} gave {member.mention} a role called: {role.name}")

@bot.command()
async def dm(ctx, user: discord.Member = None, *, arg = None):
  await ctx.message.delete()
  if user == None:
    await ctx.send("Please mention a user.")
  elif arg == None:
    await ctx.send("Please enter a message.")
  else:
    await user.send(arg)

@bot.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def _kickuser(ctx, user: discord.Member = None, *, arg = None):
    if ctx.author.guild_permissions.kick_members == True:
        if user is None:
            await ctx.send(":thonk: Provide a user to kick.")    
            return False
        if arg is None:
            await ctx.send(":reason: I need a reason to kick: **{}**".format(user.name))
            return False
        reason = arg
        author = ctx.author
        await user.kick()
        embed = discord.Embed(title=":Successfully Kicked!", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url=random.choice(['https://media.giphy.com/media/m9eG1qVjvN56H0MXt8/giphy.gif', 'https://media.giphy.com/media/UrcXN0zTfzTPi/giphy.gif', 'https://media.giphy.com/media/7DzlajZNY5D0I/giphy.gif']))
        await ctx.send(embed=embed)
    else:
        await ctx.send("You Don't have Permissions!")


@bot.command()
async def spoil(ctx, *, reason):
   await ctx.send(f"||{reason}||")

@bot.command()
async def ud(ctx, *, reason):
   embed = discord.Embed(title="ok")
   embed.add_field(name="Test", value=client.get_random_definition())
   await ctx.send(embed=embed)

@bot.command()
async def top30(ctx):
    with open('money.json', 'r') as f:
        users = json.load(f)
        highscore = sorted(users, key=lambda x : users[x].get('money', 0), reverse=True)
        for number, user in enumerate(highscore[:30]):
            member = await bot.fetch_user(user)
            exp_format = "{:,}".format(users[user].get('money', 0))
            embed = discord.Embed(title=f"{ctx.guild.name}'s Value Highscores", description=f"Shows the top 30 people that have contributed.", colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=ctx.guild.icon_url)
        for number, user in enumerate(highscore[:30]):
            member = await bot.fetch_user(user)
            exp_format = "{:,}".format(users[user].get('money', 0))
            embed.add_field(name=f'hel',value='**{0}.** {2} - ${1}\n'.format(number + 1, exp_format, member.mention),inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def pypi(ctx, *, module : str):
    pkg = get_pkg_info(module)
    embed=discord.Embed(title=f'PyPI Package - {pkg.name}', url=pkg.url)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png')
    embed.add_field(name='Package version:', value=pkg.version, inline=False)
    embed.add_field(name='Package info:', value=pkg.summary, inline=False)
    embed.set_footer(text=f'Created by: {pkg.author.name}')
    await ctx.send(embed=embed)

@bot.command()
async def clearchat(ctx, amount: int):
    channel = discord.utils.get(ctx.guild.channels, name="logs-reports")
    guild = ctx.guild
    author = ctx.author
    embed = discord.Embed(
        title = 'Cleared Messages Report',
        description = '',
        color=ctx.message.author.top_role.colour)
    embed.add_field(name=f'Cleared by:', value=(author.mention), inline=False)
    embed.add_field(name='Messages Cleared:', value=(amount), inline=False)
    channel
    embed.set_footer(text=datetime.datetime.now())
    await channel.send(embed=embed)  
    await ctx.channel.purge(limit=amount)

@bot.command()
async def status(ctx, typed, *, name):
  await ctx.message.delete()
  activity = discord.Activity(name=f'{name}', type=getattr(ActivityType, typed, 'unknown'))
  await bot.change_presence(activity=activity)
  await ctx.send(f"Status has been changed to {typed} | {name}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
 await ctx.channel.purge(limit=amount)

@bot.command()
async def advertisement(ctx):
   await ctx.message.delete()
   embed = discord.Embed(title="Meepo Invite Me!", description=f"> Created By: **Steveo#0068** Main Helper: **Username#0101**\n***Features:***\n\n:tada: **Host Giveaways**\n:bulb: **Smart & Useful commands**\n:gear: **Util Commands (Mainly focused)**\n:calendar_spiral: **Updating Regularly**\n:up: **Uptime of 24/7**\n:bangbang: **Ban/Kick/Warn Commands**\n\n**Links**\n[Top.gg Link](https://top.gg/bot/680674076905177119)\n[Invite Link](https://discordapp.com/oauth2/authorize?client_id=680674076905177119&scope=bot)\n[Support Server](https://discord.gg/3JGUdPR)\n\n**[!] Friendly Reminder:** If you have any suggestions on what to add to the bot please contact **Steveo#0068** directly into PMs, it would be appreciated!")
   await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def changelog(ctx, *, message):
 for guild in bot.guilds:
  for channel in guild.channels:
    if channel.name == "meepo-zone":
      try:
        await channel.send(message)
        print(f"{guild} got the changelog.")
      except:
          print(f"{guild} didn't get the changelog.")
print("Action Completed.")

@bot.command()
@commands.is_owner()
async def bc(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"{user.name} has recieved the message.")
        except:
            print(f"{user.name} has NOT recieved the message.")
    print("Action Completed")

@bot.command()
async def search(ctx, *, query):
    video = danksearch.Video(advanced = True) 
    await video.search(query)
    embed=discord.Embed()
    embed.set_image(url=video.thumbnail)
    embed.add_field(name="Title",value=video.title)
    embed.add_field(name="Watch",value="[Click here to watch]({})".format(video.url), inline=False)
    embed.add_field(name="Views",value=video.views, inline=False)
    embed.add_field(name="Likes",value=video.likes, inline=False)
    embed.add_field(name="Dislikes",value=video.dislikes, inline=False)
    embed.add_field(name="Creator",value=video.creator, inline=False)
    embed.add_field(name="Channel",value="[link]({})".format(video.channel))
    await ctx.send(embed=embed)
@bot.command()
async def description(ctx, *, query):
    video=Video(advanced=True)
    await video.search(query)
    await ctx.send(f"""```
    Description: {video.description}```
    """)

@bot.event
async def on_member_update(before, after):
  channel = discord.utils.get(before.guild.text_channels, name="logs-reports")
  roles = [role for role in before.roles]
  roless = [role for role in after.roles]

  if before.roles != after.roles:
    embed = discord.Embed(color=before.colour, description=f"{before}'s Roles Change")
    embed.set_author(name=f"{before} ({before.id})", icon_url=before.avatar_url)
    embed.add_field(name=f"**Before:** ( {len(before.roles)} ) :", value=" ".join([role.mention for role in roles]))
    embed.add_field(name=f"**After:** ( {len(after.roles)} ) :", value=" ".join([role.mention for role in roless]))
    embed.set_footer(text=f"{datetime.datetime.now()}")
    await channel.send(embed=embed)  
  elif channel is None:
    return  
  else:
    return

@bot.command()
async def value_help(ctx):
   embed = discord.Embed(title="**Help Commands**", description="Current Value commands of '`Meepo`', to use a command the global prefix is `??` `<cmmand>`, any problems contact **Steveo#0068**")
   embed.add_field(name=":moneybag: **Value Bot Module** - `Enabled`", value="This module helps your faction members keep on track of how much money they have deposited. Knowing if they actually add realm value or not.", inline=False)
   embed.add_field(name="??deposit <amount>", value="**Deposits money into your total score", inline=False)
   embed.add_field(name="??top30", value="**Shows total 30 people who have contributed.**", inline=False)
   embed.add_field(name="??remove <user> <amount>", value="**Removes money from that user/your total score.**", inline=False)
   await ctx.send(embed=embed)


@bot.command()
async def remove(ctx, member: discord.Member, amount: int):
  with open("money.json", "r") as f:
    money = json.load(f)
  
  await money_update(money, member)
  await money_remove(money, member, amount)
  
  balance = money[str(member.id)]["money"]
  xyz = "{:0,}".format(int(balance))
  comma = "{:0,}".format(int(amount))
  await ctx.send(f'{ctx.author.mention} removed {comma}$ out of {member.mention} deposits. Total Score: {xyz}$')

  with open("money.json", "w") as f:
    json.dump(money, f)

async def money_update(users, user): #users is the json name
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]["money"] = 0

async def money_remove(users, user, amount):
  users[str(user.id)]["money"]  -= amount

@bot.command()
async def forceremove(ctx, amount: int):
  with open("money.json", "r") as f:
    money = json.load(f)
  
  await money_update(money, ctx.author)
  await money_remove(money, ctx.author, amount)
  
  balance = money[str(ctx.author.id)]["money"]
  xyz = "{:0,}".format(int(balance))
  comma = "{:0,}".format(int(amount))
  remover = ctx.author
  await ctx.send(f'{remover} removed {amount}$ out of {member.mention}s deposits. Total Score: {xyz}$')

  with open("money.json", "w") as f:
    json.dump(money, f)

async def money_update(users, user): #users is the json name
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]["money"] = 0

async def money_remove(users, user, amount):
  users[str(user.id)]["money"]  -= amount
        
@bot.command()
async def deposit(ctx, amount: int):
  await ctx.message.delete()
  with open("money.json", "r") as f:
    money = json.load(f)
  
  await money_update(money, ctx.author)
  await money_add(money, ctx.author, amount)
  
  balance = money[str(ctx.author.id)]["money"]
  xyz = "{:0,}".format(int(balance))
  comma = "{:0,}".format(int(amount))
  embed = discord.Embed(title=f"➕ **{ctx.author} deposited money using** `/deposit`.", colour=ctx.author.top_role.colour)
  embed.add_field(name='Added By', value=f"**{ctx.author.mention}**", inline=True)
  embed.add_field(name='Added value', value=f"{amount} = {comma} $", inline=True)
  embed.add_field(name="Your Total", value=f"{xyz} $")
  # How do i make a section of the 'args' so i can make a reason to report
  embed.set_footer(text="{}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

  with open("money.json", "w") as f:
    json.dump(money, f)

async def money_update(users, user): #users is the json name
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]["money"] = 0

async def money_add(users, user, amount):
  users[str(user.id)]["money"]  += amount

@bot.command()
async def giveaway(ctx, day, win, date, *, reason):
    await ctx.message.delete() 
    embed = discord.Embed(title=':tada: **Giveaway Active** <:5488_OveEyesOFF:574158618669350912>', color=ctx.author.top_role.colour, timestamp=ctx.message.created_at)
    embed.add_field(name='Hosting:', value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name='Duration:', value=f"**{day}** Day(s)", inline=True)
    embed.add_field(name='Winners:', value=f"**{win}** ", inline=True)
    embed.add_field(name='Date Stated:', value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
    embed.add_field(name='Date Ending:', value=f"{date}", inline=False)
    embed.add_field(name='Description:', value=f"{reason}", inline=False)
    embed.add_field(name='Requirement To Enter:', value="React With <:1641_Sino:702079170510848011>   to enter!", inline=False)
    # How do i make a section of the 'args' so i can make a reason to report
    embed.set_footer(text=f"GA: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("<:1641_Sino:702079170510848011>")
@bot.command()
async def choosewinner(ctx, msg, winnerss: int=1):
    msg=await ctx.channel.fetch_message(int(msg))
    if msg:

        data=[reaction for reaction in msg.reactions if str(reaction.emoji)=="<:1641_Sino:702079170510848011>"]
        if len(data)==0:
          return 
        users=[]
        async for user in data[0].users():
            if not user.bot:
                users.append(user)
        winners=[]
        for i in range(winnerss):
            winner=random.choice(users)
            winners.append(winner.mention)
            users.pop(users.index(winner))
        embed = discord.Embed(title=":tada: Giveaway ended :tada:")
        embed.add_field(name="Hosted By:", value=f"{ctx.author.mention} ID: [{ctx.author.id}]", inline=False)
        embed.add_field(name="Winners:", value=f"{','.join(winners)}", inline=False)
        embed.add_field(name="Date Recorded:", value=datetime.datetime.now(), inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def joined(ctx, member: discord.Member):
   embed = discord.Embed(title=f"{member.name} Joined {ctx.guild.name} at", description=member.joined_at.strftime("%A, %B %d %Y %H:%M%p"))
   embed.set_thumbnail(url=member.avatar_url)
   embed.set_footer(text=f'You: {ctx.author.name} | User: {member} | {ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC")}')
   await ctx.send(embed=embed)

@bot.command()
async def depositspawners(ctx, amount: int, *, reason=None):
  with open("money.json", "r") as f:
    money = json.load(f)
  
  await money_update(money, ctx.author)
  await money_add(money, ctx.author, amount)
  
  balance = money[str(ctx.author.id)]["money"]
  xyz = "{:0,}".format(int(balance))
  comma = "{:0,}".format(int(amount))
  embed = discord.Embed(title=f"➕ **{ctx.author} deposited money using** `/deposit`.", colour=ctx.author.top_role.colour)
  embed.add_field(name='Added By', value=f"**{ctx.author.mention}**", inline=True)
  embed.add_field(name='Added value', value=f"{amount} (x{reason}) = {comma} $", inline=True)
  embed.add_field(name="Your Total", value=f"{xyz} $")
  # How do i make a section of the 'args' so i can make a reason to report
  embed.set_footer(text="{}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

  with open("money.json", "w") as f:
    json.dump(money, f)

async def money_update(users, user): #users is the json name
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]["money"] = 0

async def money_add(users, user, amount):
  users[str(user.id)]["money"]  += amount

@bot.command()
async def banword(ctx, *, arg = None):
  with open("words.json", "r") as f:
    anti = json.load(f)

  if arg == None:
    return await ctx.send("`[prefix]banword [word]`")

  if not str(ctx.guild.id) in anti:
    
    anti[str(ctx.guild.id)] = {}
    banned_words = anti[str(ctx.guild.id)]["banwords"] = []
    banned_words.append(arg)

    with open("words.json", "w") as f:
      json.dump(anti, f, indent = 4)

    await ctx.send(f"`{arg}` has been added to the banned word.")

  else:

    anti[str(ctx.guild.id)]["banwords"].append(arg)
    
    with open("words.json", "w") as f:
      json.dump(anti, f, indent = 4)

    await ctx.send(f"`{arg}` has been added to the banned word.")

@bot.command()
@commands.is_owner()
async def bot_leave(ctx):
   await ctx.send("Leaving the server")
   await ctx.guild.leave()
   print(f"I left {ctx.guild.name}")


@bot.command(aliases=['kill', 'stop'])
@commands.is_owner()
async def botpause(ctx):
    msg = await ctx.send("Are you sure you want to pause the bot?")
    await msg.add_reaction(emoji="✅")
    await msg.add_reaction(emoji="❌")

    def check(_reaction, _user):
        return _user == ctx.message.author and str(_reaction.emoji) == '✅'

    try:
        _reaction, _user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('<:redtick:506537775642968095> - You took to long adding a reaction')
    else:
        bot.kill()
        await ctx.send("✅ - Successfully paused the bot")

@bot.command(aliases=['nitro'])
async def free(ctx):
    msg = await ctx.send("React for free nitro!")
    await msg.add_reaction(emoji="✅")
    await msg.add_reaction(emoji="❌")

    def check(_reaction, _user):
        return _user == ctx.message.author and str(_reaction.emoji) == '✅'

    try:
        _reaction, _user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('no lck b')
    else:
        await ctx.send(f"{ctx.author.mention} **Was PRANKED!**, no nitro 4 u!")



@bot.command(aliases=["lookup"])
async def google(ctx, *, googlesearch: str = None):
   if googlesearch == None:
      await ctx.send(f"You didn't give me anything to google *smh*")
   else:
      string = f"https://www.google.com/search?q={googlesearch}"
      await ctx.send(string.replace(" ", "+"))

@bot.command(aliases=["jokes"])
async def joke(ctx):
    await ctx.send(get_joke())

@bot.command()
async def top(ctx):
    with open('money.json', 'r') as f:
        users = json.load(f)
        highscore = sorted(users, key=lambda x : users[x].get('money', 0), reverse=True)
        for number, user in enumerate(highscore[:30]):
            member = await bot.fetch_user(user)
            exp_format = "{:,}".format(users[user].get('money', 0))
            embed = discord.Embed(title=f"{ctx.guild.name}'s Value Highscores", description=f"Value Module:  `ENABLED`", colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=ctx.guild.icon_url)
        for number, user in enumerate(highscore[:30]):
            member = await bot.fetch_user(user)
            exp_format = "{:,}".format(users[user].get('money', 0))
            embed.add_field(name=f'**{member.name}**',value='**{0}.** ${1}\n'.format(number + 1, exp_format),inline=False)
        await ctx.send(embed=embed)

@bot.command(aliases=["reboot"])
@commands.is_owner()
async def restart(ctx):
    embed = discord.Embed(title="", description=f"<:314691591484866560:714390327225745499>  Bot is restarting...")
    await ctx.send(embed=embed)
    os.execv(sys.executable, [sys.executable] + sys.argv)

@bot.command()
async def clear23(ctx):
  await ctx.message.delete()
  with open("walls.json", "r") as f:
    points = json.load(f)
  
  await points_update(points, ctx.author)
  await points_add(points, ctx.author, 1)

  score = points[str(ctx.author.id)]["score"]
  xyz = "{:0,}".format(int(score))
  embed = discord.Embed(title=f":white_check_mark: **{ctx.author.name}** marked walls as clear using: `/clear`", colour=ctx.author.top_role.colour)
  embed.add_field(name='**Checked By**', value=f"**{ctx.author.mention}**", inline=False)
  embed.add_field(name='**Score**', value=f"{xyz}", inline=False)
  embed.add_field(name="**Time Checked**", value=ctx.message.created_at.strftime("%a, %#d %B %Y, %I:%M UTC"), inline=False)
  embed.set_footer(text="{}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.send(embed=embed)

  with open("walls.json", "w") as f:
    json.dump(points, f)
    f.close()

async def points_update(users, user): #users is the json name
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]["score"] = 0
    return users
async def points_add(users, user, points):
  users[str(user.id)]["score"]  += points
  return users

@bot.command()
async def suggest(ctx, *, reason=None):
   await ctx.message.delete()
   embed = discord.Embed(title=f"", description=f"{reason}")
   embed.set_footer(text=ctx.message.created_at.strftime("%#d %b %Y"), icon_url=ctx.guild.icon_url)
   embed.set_author(name=f"{ctx.author} - Suggestion", icon_url=ctx.author.avatar_url)
   msg = await ctx.send(embed=embed)
   await msg.add_reaction("<:6940_agree:702035143472447548>")
   await msg.add_reaction("<:1665_disagree:702035123541114921>")

@bot.command()
async def topwallchecks(ctx):
    with open('walls.json', 'r') as f:
        users = json.load(f)
        highscore = sorted(users, key=lambda x : users[x].get('score', 0), reverse=True)
        for number, user in enumerate(highscore[:15]):
            member = await bot.fetch_user(user)
            exp_format = "{:,}".format(users[user].get('score', 0))
            embed = discord.Embed(title=f"<:5221_mycoolessdsd:706129653491826689>  {ctx.guild.name}'s Wall Check Highscores", description=f"**Scores:**", colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(url='https://i.imgur.com/oAJOKSy.jpg')
        for number, user in enumerate(highscore[:15]):
            member = await bot.fetch_user(user)
            exp_format = "{:,}".format(users[user].get('score', 0))
            embed.add_field(name=f'**{member.name}**',value='**{0}.** Score: {1}\n'.format(number + 1, exp_format),inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def depositadmin(ctx, member: discord.Member, amount: int):
  await ctx.message.delete()
  with open("money.json", "r") as f:
    money = json.load(f)
  
  await money_update(money, member)
  await money_add(money, member, amount)
  
  balance = money[str(member.id)]["money"]
  xyz = "{:0,}".format(int(balance))
  comma = "{:0,}".format(int(amount))
  embed = discord.Embed(title=f"➕ **{member} deposited money using** `/deposit`.", colour=ctx.author.top_role.colour)
  embed.add_field(name='Added By', value=f"**{ctx.author.mention}**", inline=True)
  embed.add_field(name='Added value', value=f"{amount} = {comma} $", inline=True)
  embed.add_field(name="Their Total", value=f"{xyz} $")
  # How do i make a section of the 'args' so i can make a reason to report
  embed.set_footer(text="{}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

  with open("money.json", "w") as f:
    json.dump(money, f)

async def money_update(users, user): #users is the json name
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]["money"] = 0

async def money_add(users, user, amount):
  users[str(user.id)]["money"]  += amount


@bot.event
async def when_mentioned(ctx):
    embed=discord.Embed(title="Hi, I'm Meepo!", description="My default prefix is `??` Hope this helps!", color=0x176cd5)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):

    if ctx.author.id == 638967080632451086:
  
      await ctx.reinvoke()
      return

    embed = discord.Embed()
    embed.title = "<:5316_Error_512x512_by_DW:725609652494270464> You are not able to run this command."
    embed.description = f"{error}"

    await ctx.send(embed = embed)

  else:

    embed = discord.Embed()
    embed.title = "<:5316_Error_512x512_by_DW:725609652494270464> Error"
    embed.description = f"{error}"

    await ctx.send(embed = embed)
  
@bot.command(pass_context=True)
async def shoot(ctx, member: discord.Member):
    """Shoot someone."""
    embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def love(ctx, member: discord.Member):
	choice = ["https://i.pinimg.com/originals/6a/a6/ac/6aa6ac736b070b735522295fa4bed23d.gif","https://i.pinimg.com/originals/4d/59/5b/4d595b493c634263506f6e3babdd0bbe.gif","https://i.pinimg.com/originals/63/bf/9e/63bf9e50d00de8f8533d7650ec5d7f30.gif","https://4.bp.blogspot.com/-dRTN0eV5Fes/UtUq-9I57PI/AAAAAAAATtM/oPRqU-3q7zA/s400/teddybear+love.gif","https://i.pinimg.com/originals/21/fc/cc/21fcccdfaaee2509b82730e21d6f94f4.gif"]
	responces = ["“I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.”","“You know you're in love when you can't fall asleep because reality is finally better than your dreams.”","“A friend is someone who knows all about you and still loves you.”","“We accept the love we think we deserve.”","“As he read, I fell in love the way you fall asleep: slowly, and then all at once.”","“Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.”","“There is never a time or place for true love. It happens accidentally, in a heartbeat, in a single flashing, throbbing moment.”","“Love is that condition in which the happiness of another person is essential to your own.”","“Love looks not with the eyes, but with the mind, And therefore is winged Cupid painted blind.”"]
	embed = discord.Embed(title=f"**{ctx.author.name}** Loves **{member.name}** <3", description=random.choice(responces))
	embed.set_image(url=random.choice(choice))
	await ctx.send(embed=embed)

@bot.command()
async def cookie(ctx, member: discord.Member):
	choice = ["http://31.media.tumblr.com/4575f6577e97dbd2d8dd4d6938d39547/tumblr_momvhfdfz71rolxxno1_500.gif","https://i.gifer.com/MRr.gif","https://media.giphy.com/media/nAErqE3k2C3fy/giphy.gif"]
	responces = ["'We are like a deck of cards; different colors and symbols but one cannot work without the whole set.'","'He gave her a look that you could have poured on a waffle'","'Don’t make love by the garden gate, love is blind but the neighbors ain’t.'"]
	embed = discord.Embed(title=f"**{ctx.author.name}** Gave a cookie to **{member.name}** Nom nom nom!", description=random.choice(responces))
	embed.set_image(url=random.choice(choice))
	await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def createchannel(ctx, channel_name='Channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await ctx.send(f'Created a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

    if existing_channel:
        await ctx.send(f'Unable to create a text channel {ctx.author.mention} - There is already a channel named **{channel_name}**')


@bot.command(name = "deletechannel")
@commands.has_permissions(administrator=True)
async def deletechannel2(ctx, channel: discord.TextChannel = None):
  if channel == None:
    return

  await channel.delete()
  await ctx.send(f"Deleted {channel.name}")
@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(title="💰 **Current Bitcoin Price (USD)**", description="Bitcoin price is: $" + response['bpi']['USD']['rate'])
        embed.add_field(name="Date Updated", value=ctx.message.created_at.strftime("%A, %#d %B %Y"))
        embed.set_thumbnail(url="https://en.bitcoin.it/w/images/en/2/29/BC_Logo_.png")
        await ctx.send(embed=embed)

@bot.command()
async def covid(ctx):
  covid = Covid()
  covid.get_data()
  time = ctx.message.created_at.strftime("%I:%M")
  stats = covid.get_total_recovered()
  embed = discord.Embed(title="Current COVID-19 Statistics")
  embed.add_field(name="**Active Cases:**", value=covid.get_total_active_cases(), inline=False)
  embed.add_field(name="**Confirmed Cases:**", value=covid.get_total_confirmed_cases(), inline=False)
  embed.add_field(name="**Recovered:**", value=f"{stats}", inline=False)
  embed.add_field(name="**Deaths:**", value=covid.get_total_deaths())
  embed.set_thumbnail(url="https://www.staugustine.edu/wp-content/uploads/2020/02/Background_01.png")
  embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
  embed.set_footer(text=f"Currently Selected Category: GLOBAL DEATH,GLOBAL RECOVERED | {time}")
  await ctx.send(embed=embed)

@bot.command()
async def covid19(ctx, arg=None):
  if arg == None:
    await ctx.send('You must define a category. **Example:** `??covid USA`.')
  elif arg == "global":
    covid = Covid()
    covid.get_data()
    time = ctx.message.created_at.strftime("%I:%M")
    stats = covid.get_total_recovered()
    embed = discord.Embed(title="Current COVID-19 Statistics")
    embed.add_field(name="**Active Cases:**", value=covid.get_total_active_cases(), inline=False)
    embed.add_field(name="**Confirmed Cases:**", value=covid.get_total_confirmed_cases(), inline=False)
    embed.add_field(name="**Recovered:**", value=f"{stats}", inline=False)
    embed.add_field(name="**Deaths:**", value=covid.get_total_deaths())
    embed.set_thumbnail(url="https://www.staugustine.edu/wp-content/uploads/2020/02/Background_01.png")
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Currently Selected Category: GLOBAL DEATH,GLOBAL RECOVERED | {time}")
    await ctx.send(embed=embed)
  elif arg == "USA":
    covid = Covid()
    covid.get_data()
    embed = discord.Embed(title="Covid-19 Statistics USA")
    embed.add_field(name="Total Cases", value=covid.get_status_by_country_name("usa"))
    await ctx.send(embed=embed)

@bot.command()
async def permissions(ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        """Shows a member's permissions in a specific channel.
        If no channel is given then it uses the current one.
        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await say_permissions(ctx, member, channel)

@bot.command()
async def startbooster(ctx, boostertype, time, min):
   embed = discord.Embed(title="Booster Time!", description=f"The faction has a **{boostertype} Booster** ready! Come On! We need your help! We're starting in {time} {min}.")
   embed.add_field(name="Alerted by", value=f"{ctx.author.mention} [{ctx.author}]", inline=False)
   embed.add_field(name="Date", value=ctx.message.created_at.strftime("%A, %#d %B %Y, %I:%M UTC"), inline=False)
   embed.set_footer(text='OP')
   await ctx.send(embed=embed)
   await ctx.send('BOOSTER ROLE NAME')

@bot.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
       await ctx.send(":x: You need to **Specify** a member to mute.")
       return
    await member.add_roles(role)
    embed = discord.Embed(title="", description=f"<:314691591484866560:714390327225745499> ***{member} has been muted***")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
       await ctx.send(":x: You need to **Specifiy** a member to unmute.")
       return
    await member.remove_roles(role)
    embed = discord.Embed(title="", description=f"<:314691591484866560:714390327225745499> ***{member} was unmuted***")
    await ctx.send(embed=embed)

@bot.command()
async def timer(ctx):
  embed = discord.Embed(description="Starting..", color = discord.Colour.light_grey())
  msg = await ctx.send(embed=embed)
  await loop(ctx, msg)

async def loop(ctx, msg):
  while True:
     time = ctx.message.created_at.strftime("%I:%M UTC")
     embed = discord.Embed(title="", description=f"⚠️ **Check now at:** `{time}`")
     await msg.edit(embed=embed)
     role = discord.utils.get(ctx.guild.roles, name="Wall Checkers")
     await ctx.send(role.mention)
     await asyncio.sleep(60)
     bot.loop.create_task(loop(ctx))

@bot.command()
async def timer1(ctx):
  embed = discord.Embed(description="Starting..", color = discord.Colour.light_grey())
  await ctx.send(embed=embed)
  await loop(ctx)

async def loop(ctx):
  while True:
     time = ctx.message.created_at.strftime("%I:%M UTC")
     embed = discord.Embed(title="", description=f"⚠️ **Check now at:** `{time}`")
     await ctx.send(embed=embed)
     role = discord.utils.get(ctx.guild.roles, name="Wall Checkers")
     await ctx.send(role.mention)
     await asyncio.sleep(60)
     bot.loop.create_task(loop(ctx))

@bot.command()
async def logout(ctx):
  await ctx.send('Please enter the password. Example: 0000')

@bot.command()
async def say(ctx, *, reason):
  await ctx.message.delete()
  await ctx.send(f'{reason}')

@bot.command()
async def replstate(ctx):
   await ctx.send('<:7881_battery_full:712829248498434149> **Repl.it/Meepo** - Current State: **97%**')

@bot.command(pass_context=True)
async def poll(ctx, *, reason=None):
   embed = discord.embed(title="", description=f"{reason}")
   embed.set_author(name=f"{ctx.author.name}'s Poll - {ctx.guild.name}", icon_url=ctx.author.avatar_url)
   msg = await ctx.send(embed=embed)
   await msg.add_reaction("<:number1:713335437866827797>")
   await msg.add_reaction("<:number2:713335461065654272>")
   await msg.add_reaction("<:number3:713335478937452636>")

@bot.command()
async def about(ctx):
   embed = discord.Embed(title="Hi! I'm Meepo.", description="Multi-Purpose funtion discord bot at your fingertips!")
   embed.add_field(name="Developer Change", value="Dave#0001 is currently running me!")
   await ctx.send(embed=embed)

for cog in os.listdir('cogs'):
  if cog.endswith('.py'):
    try:
      cog = f"cogs.{cog.replace('.py', '')}"
      bot.load_extension(cog)
      
    except Exception as e:
      print(f'{cog} loading failed.')
      raise 

keep_alive()
bot.run("NjgwNjc0MDc2OTA1MTc3MTE5.XvsA0A.684uJxSwTyd3piNoOEMY4SB3ayY")
