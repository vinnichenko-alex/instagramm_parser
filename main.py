import instaloader

bot = instaloader.Instaloader()

USER = 'lika.copik'
LOGIN = 'test_forpython'
PASSWORD = 'test1211'
bot.login(LOGIN, PASSWORD)
bot.download_profile(USER, download_stories_only=True)
