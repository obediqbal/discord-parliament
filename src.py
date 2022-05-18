import discord
intents = discord.Intents.default()
intents.members = True
from discord.ext import commands
from discord.ui import Button

client = commands.Bot()


# class Buttons(discord.ui.View):
#     def __init__(self, *, timeout=180):
#         super().__init_(timeout=timeout)
#     @discord.ui.button(label="Button", style=discord.ButtonStyle.gray)
#     async def gray_button(self, button:discord.ui.Button, interaction:discord.Interaction):
#         await interaction.response.edit_message(content=f'This is an edited button response!')




# @client.command()
# async def button(ctx):
    # await ctx.send("This message has buttons!", view=Button())