import discord
import requests

from discord.ext import commands,tasks

class GitHubStarsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Create a private, audio channel called "github stars" in the "Server Stats" category
        server = self.bot.get_guild(920056098122248193)
        category = discord.utils.get(server.categories, name="Server Stats")
        moderator_role = discord.utils.get(server.roles, name="TA Mods")

        # Make it so that only users with the "Moderator" role can connect to the channel
        overwrites = {
            server.default_role: discord.PermissionOverwrite(connect=False),
            moderator_role: discord.PermissionOverwrite(connect=True),
        }
        github_stars_channel = await server.create_voice_channel("github stars", category=category, overwrites=overwrites, position=0)

        # Get the number of stars for the GitHub repository
        repo_url = "https://api.github.com/repos/tubearchivist/tubearchivist"
        response = requests.get(repo_url)
        data = response.json()
        stars = data["stargazers_count"]

        # Rename the channel to "GitHub-Stars" and append the number of stars
        await github_stars_channel.edit(name=f"GitHub-Stars ({stars})")

    @tasks.loop(hours=1.0)
    async def update_stars(self):
        # Get the GitHub repository channel
        github_stars_channel = self.bot.get_channel(YOUR_GITHUB_STARS_CHANNEL_ID)

        # Get the number of stars for the GitHub repository
        repo_url = "https://api.github.com/repos/tubearchivist/tubearchivist"
        response = requests.get(repo_url)
        data = response.json()
        stars = data["stargazers_count"]

        # Rename the channel to "GitHub-Stars" and append the updated number of stars
        await github_stars_channel.edit(name=f"GitHub-Stars ({stars})")

def setup(bot):
    bot.add_cog(GitHubStarsCog(bot))
