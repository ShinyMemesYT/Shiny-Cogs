import discord
import asyncio
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, user : discord.Member):
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    async def on_member_join(discord.Member):
        add_roles(member, "Members")

def setup(bot):
    bot.add_cog(Mycog(bot))
