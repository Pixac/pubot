import nextcord
from nextcord.ext import commands
from keep_alive import keep_alive

client = nextcord.Client()
intents = nextcord.Intents().all()
client = commands.Bot(command_prefix='-_- ', help_command=None, intents= intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=nextcord.Game ('Minecraft'))

@client.command()
async def ping(ctx):
  await ctx.send("Up and running!")

@client.event
async def on_member_join(member):
  guild = client.get_guild(881800984173637642)
  channel = client.get_channel(882529731029905438)
  await client.get_channel(882531698343026699).send(f"Welcome, {member.mention} to {guild.name}! Please read the {channel.mention} to get started.")

@client.event
async def on_member_remove(member):
  await client.get_channel(882531008396808273).send(f"sorry to see you go {member.mention}. It was fun while you were here.")

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.content == "-_- purge100":
    await message.channel.purge(limit=100)



keep_alive()
client.run('ODMxNzczOTEwODMxNTk1NTIw.YHaH0Q.YD_SfNg8ds9U0o0LwCIFrVlj9lI')