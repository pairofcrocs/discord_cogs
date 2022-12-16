from .githubstars import githubstars


def setup(bot):
    bot.add_cog(githubstars(bot))
