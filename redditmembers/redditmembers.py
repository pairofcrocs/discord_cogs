import requests
import discord
from redbot.core import commands

class RedditSubscriberCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create_channel(self, ctx):
        response = requests.get(
            url = 'https://www.reddit.com/r/TubeArchivist/about.json',
            headers ={'User-agent': 'subscriber tracker bot 0.0.1'})

        subscribers = response.json()['data']['subscribers']

        guild = ctx.guild

        channel_created = await ctx.guild.create_voice_channel("subscribers")

def setup(bot):
    bot.add_cog(RedditSubscriberCog(bot))
