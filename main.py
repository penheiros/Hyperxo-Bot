import discord
from discord import activity
from discord.ext import commands
from discord import Color as col

token = "ODg5MDYxNTE2NDg0MTY5NzM5.YUbxDw.socvb_X-0dx7q_lhRUFacCp79t4"
activity = discord.Game(name="One tapping in Iron lobby | -help")
client = commands.Bot(command_prefix="-", activity=activity, help_command=None)

@client.event
async def on_ready():
    print("Hyperxo Bot Online")


@commands.has_any_role('HE | Owner', 'HE | Co-Owner', 'HE | Management', "HE | Developer")
@client.command()
async def announce(ctx, *, arg):
    information = arg
    to_announce = information if '=' not in information else information.split('=')[0]

    announcement_channel_info = 887745818654818375 if '=' not in information else information.split('=')[1]
    announcement_id = int(''.join([number for number in str(announcement_channel_info) if number.isnumeric()]))
    announcement_channel = client.get_channel(announcement_id)

    await announcement_channel.send(to_announce)
    await ctx.message.delete()
    await ctx.send(f":white_check_mark: Your announcement has been posted in <#{announcement_id}>")



client.run(token)