from src import client

class Member():
    def __init__(self, guild, user):
        self.guild = guild
        self.user = user
        self.is_voter = False


    def update_data(self):
        self.guild = client.get_guild(self.guild.id)
        self.user = self.guild.get_member(self.user.id)
