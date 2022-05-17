from utils import client
import auth
import data


@client.event
async def on_ready():
    print('ready!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    member_instance = data.get_member(message.guild, message.author)


client.run(auth.token)