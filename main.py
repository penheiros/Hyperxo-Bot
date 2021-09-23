import discord
from discord import activity
from discord.ext import commands
from discord import Color as col

token = "ODg5MDYxNTE2NDg0MTY5NzM5.YUbxDw.WbHpZTUNCkC27W6BrS32kyU3EN0"
activity = discord.Game(name="Valorant | -help")
client = commands.Bot(command_prefix="-", activity=activity)

@client.event
async def on_ready():
    print("Hyperxo Bot Online")


@commands.has_any_role('HE | Owner', 'HE | Co-Owner', 'HE | Management', "HE | Developer")
@client.command()
async def announce(ctx, *, arg):
    information = arg
    to_announce = information if '||' not in information else information.split('||')[0]

    announcement_channel_info = 887745818654818375 if '||' not in information else information.split('||')[1]
    announcement_id = int(''.join([number for number in str(announcement_channel_info) if number.isnumeric()]))
    announcement_channel = client.get_channel(announcement_id)

    await ctx.message.delete()
    await announcement_channel.send(to_announce)
    await ctx.send(f":white_check_mark: Your announcement has been posted in <#{announcement_id}>")


@commands.has_any_role('HE | Owner', 'HE | Co-Owner', 'HE | Management', "HE | Developer")
@client.command()
async def embedannounce(ctx, *, arg):
    #first check what kind of embed it is
    embed = discord.Embed(color=col.green())
    embed_type = 'banner' if 'banner' in arg else 'message'

    #if its banner then send the image
    if embed_type == 'banner':
        if arg.count('||') > 1:
            announcement_channel_id = int(''.join([number for number in str(arg.split('||')[2]) if number.isnumeric()]))
        else:
            announcement_channel_id = 887745995297918976

        announcement_channel = client.get_channel(announcement_channel_id)
        banner_link = arg.split('||')[1]
        embed.set_image(url=str(banner_link))
        await announcement_channel.send(embed=embed)
    else:
        print('error')

client.run(token)