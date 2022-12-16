from .githubstars import GithubStarsCog


def setup(bot):
    bot.add_cog(githubstars(bot))
