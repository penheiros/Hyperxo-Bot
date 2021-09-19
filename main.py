import discord
from discord import activity
from discord.ext import commands
from discord import Color as col

token = "ODg5MDYxNTE2NDg0MTY5NzM5.YUbxDw.c_u0Hm6i8uTTMtPMZNcyX13buAc"
activity = discord.Game(name="One tapping in Iron lobby | -help")
client = commands.Bot(command_prefix="-", activity=activity, help_command=None)

@client.event
async def on_ready():
    print("Hyperxo Bot Online")


@commands.has_any_role('HE | Owner', 'HE | Co-Owner', 'HE | Management', "HE | Developer")
@client.command()
async def announce(ctx, *, arg):
    information = arg 
    desired_channel = information.split('-')[1] if '-' in information else 887745818654818375
    print(desired_channel)





client.run(token)