import discord
from discord import activity
from discord.ext import commands
from discord import Color as col

token = ""
activity = discord.Game(name="Valorant | -help")
client = commands.Bot(command_prefix="-", activity=activity)

@client.event
async def on_ready():
    print("Hyperxo Bot Online")


@commands.has_any_role('HE | Owner', 'HE | Co-Owner', 'HE | Management', "HE | Developer")
@client.command(brief="Command to send announcements, type -help announce for more info!",
description="To send an announcement type: -announce <message here>\nNote: These command has a default channel, if you want to post them in a different channel, at the end of the command put: || <channel here>")
async def announce(ctx, *, arg):
    information = arg
    to_announce = information if '||' not in information else information.split('||')[0]

    announcement_channel_info = 887745818654818375 if '||' not in information else information.split('||')[1]
    announcement_channel_id = int(''.join([number for number in str(announcement_channel_info) if number.isnumeric()]))
    announcement_channel = client.get_channel(announcement_channel_id)

    await announcement_channel.send(to_announce)
    await ctx.send(f":white_check_mark: Your announcement has been posted in <#{announcement_channel_id}>")


@commands.has_any_role('HE | Owner', 'HE | Co-Owner', 'HE | Management', "HE | Developer")
@client.command(aliases=['ea'], brief='Command to send embed announcements, type -help embedannounce for more info!', 
description='To send a poster/banner, use this method: -embedannounce banner || <banner link here>\nTo send normal embed announcement, use this method: -embedannounce message || <type anything here>\nNote: These commands have default channels, if you want to post them in a different channel, at the end of the command put: || <channel here>')
async def embedannounce(ctx, *, arg):
    #first check what kind of embed it is
    embed_type = 'banner' if 'banner' in arg else 'message'

    if arg.count('||') > 1:
        announcement_channel_id = int(''.join([number for number in str(arg.split('||')[2]) if number.isnumeric()]))
    else:
        announcement_channel_id = 887745995297918976

    announcement_channel = client.get_channel(announcement_channel_id)

    if embed_type == 'banner':
        banner_link = arg.split('||')[1]
        banner_embed = discord.Embed(color=col.teal())
        banner_embed.set_image(url=str(banner_link))
        await announcement_channel.send(embed=banner_embed)

    elif embed_type == 'message':
        message_info = arg.split('||')[1]
        message_embed = discord.Embed(description=message_info, color=col.teal())
        await announcement_channel.send(embed=message_embed)

    await ctx.send(f":white_check_mark: Your announcement has been posted in <#{announcement_channel_id}>")


client.run(token)