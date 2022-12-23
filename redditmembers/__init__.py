from .githubstars import RedditSubscriberCog

def setup(bot):
    bot.add_cog(RedditSubscriberCog(bot))
