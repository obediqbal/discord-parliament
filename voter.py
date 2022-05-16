voters = {}

class Voter:
    def __init__(self, member):
        self.id = member.id
        self.name = member.name
        self.last_active = 0