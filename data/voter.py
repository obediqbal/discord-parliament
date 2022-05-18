from data.data import Member

class Voter(Member):
    def __init__(self, guild, user, last_active):
        super().__init__(guild, user)
        self.last_active = last_active
        self.is_voter = True
