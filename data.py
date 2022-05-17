from utils import client
from utils import has_voter_role

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


class Member():
    def __init__(self, guild, user):
        self.guild = guild
        self.user = user
        self.is_voter = False


    def update_data(self):
        self.guild = client.get_guild(self.guild.id)
        self.user = self.guild.get_member(self.user.id)


class Voter(Member):
    def __init__(self, guild, user, last_active):
        super().__init__(guild, user)
        self.last_active = last_active
        self.is_voter = True
