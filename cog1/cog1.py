import discord
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self):
        await self.bot.say("Bot is up and running!")

    @commands.command()
    async def punch(self, user : discord.Member):
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")


def setup(bot):
    bot.add_cog(Mycog(bot))
