import discord
import asyncio
from discord.ext import commands

class Mycog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, user : discord.Member):
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    @asyncio.coroutine
    def welcome(user):
        m = config['welcome_message'].format(
                name = user.name,
                mention_name = user.mention,
                id = user.id,
                )
        if public_channel is not None:
            yield from self.bot.say(public_channel, m)

    @asyncio.coroutine
    def help_message(user):
        m = config['help_message'].format(
                name = user.name,
                mention_name = user.mention,
                id = user.id,
                )
        yield from self.bot.say(user, m)

    @self.bot.listen
    @asyncio.coroutine
    def on_member_join(member):
        server = member.server
        if server.id != config['server']:
            return

        # debug!
        print('{} [id = {}] joined the server'.format(member.name, member.id))

        yield from help_message(member)
        yield from welcome(member)


def setup(bot):
    bot.add_cog(Mycog(bot))
