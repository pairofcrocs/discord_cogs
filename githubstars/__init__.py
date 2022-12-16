from .githubstars import GithubStarsCog

def setup(bot):
    bot.add_cog(GithubStarsCog(bot))
