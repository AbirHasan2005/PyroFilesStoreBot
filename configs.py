# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.getenv("API_ID", 12345))
	API_HASH = os.getenv("API_HASH", 'abc123')
	BOT_TOKEN = os.getenv("BOT_TOKEN", '142:adn4')
	BOT_USERNAME = os.getenv("BOT_USERNAME", 'filerobot')
	DB_CHANNEL = int(os.getenv("DB_CHANNEL", -100122))
	BOT_OWNER = int(os.getenv("BOT_OWNER", 1024552))
	DATABASE_URL = os.getenv("DATABASE_URL", 'srv+mongo')
	UPDATES_CHANNEL = int(os.getenv("UPDATES_CHANNEL", -100321 ))
	LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -100200))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @AbirHasan2005

👥 **Support Group:** [Linux Repositories](https://t.me/linux_repo)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
