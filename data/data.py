from src import client
from data.member import Member
from data.voter import Voter

guilds = {}

def recognize_guild(guild):
    """Will register Guild into guilds if it hasn't been registered yet"""
    if guild.id not in guilds.keys():
        guilds.update({guild.id : {}})


def get_member(guild, author):
    """Will register User into respective guilds if it hasn't been registered yet"""
    recognize_guild(guild)

    if author.id not in guilds[guild.id].keys():
        if has_voter_role(author):
            instance = Voter(guild, author, 0)
        else:
            instance = Member(guild, author)
        guilds[guild.id].update({author.id : instance})
    else:
        instance = guilds[guild.id][author.id]
    return instance


def has_role(user, target):
    for role in user.roles:
        if role.name==target:
            return True
    return False


def has_voter_role(user):
    return has_role(user, 'Voter')
