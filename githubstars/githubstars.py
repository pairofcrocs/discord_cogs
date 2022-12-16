import discord
import aiohttp
import asyncio
import redbot
from redbot.core import commands

channel = "Github Stars"
repository = "https://api.github.com/repos/tubearchivist/tubearchivist"

class GithubStarsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.bot.loop.create_task(self.update_github_stars_loop(channel, repository))  # start the looping task

    async def create_github_stars_channel(self, ctx):
        category = ctx.guild.get_channel(name="Server Stats")
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(connect=False)
        }
        return await ctx.guild.create_voice_channel("Github Stars", category=category, overwrites=overwrites)

    async def update_github_stars(self, channel, repository):
        async with self.session.get(f"https://api.github.com/repos/tubearchivist/tubearchivist") as resp:
            data = await resp.json()
            stars = data["stargazers_count"]
            await channel.edit(name=f"Github Stars: {stars}")

    async def update_github_stars_loop(self, channel, repository):
        while True:
            try:
                await self.update_github_stars(channel, repository)
            except Exception as e:
                print(f"An error occurred while updating Github stars: {e}")
            await asyncio.sleep(3600)  # pause for 1 hour

def setup(bot):
    bot.add_cog(GithubStarsCog(bot))
