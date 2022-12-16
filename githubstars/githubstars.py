import discord
import aiohttp
from discord.ext import commands
from discord.utils import get
from redbot.core.tasks import tasks

class GithubStarsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

async def create_github_stars_channel(self, ctx):
    category = get(ctx.guild.categories, name="Server Stats")
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(connect=False)
    }
    return await ctx.guild.create_voice_channel("Github Stars", category=category, overwrites=overwrites)

async def update_github_stars(self, channel, repository):
    async with self.session.get(f"https://api.github.com/repos/{repository}") as resp:
        data = await resp.json()
        stars = data["stargazers_count"]
        await channel.edit(name=f"Github Stars: {stars}")

    @tasks.loop(hours=1)
    async def update_github_stars_loop(self, channel, repository):
        await self.update_github_stars(channel, repository)

def setup(bot):
    bot.add_cog(GithubStarsCog(bot))
