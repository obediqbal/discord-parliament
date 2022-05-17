import discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def has_role(user, target):
    for role in user.roles:
        if role.name==target:
            return True
    return False


def has_voter_role(user):
    return has_role(user, 'Voter')