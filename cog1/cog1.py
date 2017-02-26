import discord
import asyncio
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, user : discord.Member):
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    if discord.on_member_join(member):
        print("User joined!")

def setup(bot):
    bot.add_cog(Mycog(bot))
