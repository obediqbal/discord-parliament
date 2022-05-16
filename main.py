import discord

client = discord.Client()

# Member
def has_role(member,target):
    for role in member.roles:
        if role.name==target.name:
            return True
    return False


def is_member_voter(member):
    return has_role(member, {'name': 'Voter'})


@client.event
async def on_ready():
    print('ready!')

@client.event
async def on_message(message):
    if is_member_voter(message.author):
        await message.channel.send('has role')

token = "OTU0OTc3MTgyMzMyMDkyNDY2.Yja9zg.uDyOdxelGZBJZEVPZaAdcxzz1ss"
client.run(token)