# PyroFilesStoreBot
This is Telegram Files Store Bot by [@AbirHasan2005](https://github.com/AbirHasan2005).

* Language: [Python3](https://www.python.org)
* Library: [Pyrogram](https://docs.pyrogram.org)

### Features:
- In PM Just Forward or Send any file it will save on Database & give you the Access Link.
- In Channel Add Bot as Admin with Edit Rights. When you will send any file or media in Channel it will Edit the Broadcast Message with Saved Link Button.
- You can also Broadcast anythings via this Bot.
- You can also Do Force Sub to a Channel to allow access the Bot.

### Demo Bot:
<a href="https://t.me/SuperFilesStoreBot"><img src="https://img.shields.io/badge/Demo-Telegram%20Bot-blue.svg?logo=telegram"></a>

## Configs:
* `API_ID` - Get this from [@TeleORG_Bot](https://t.me/TeleORG_Bot)
* `API_HASH` - Get this from [@TeleORG_Bot](https://t.me/TeleORG_Bot)
* `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
* `BOT_USERNAME` - Your Bot's Username. *(Without [@])*
* `DB_CHANNEL` - The Channel ID which will be used as Database
* `BOT_OWNER` - Bot Owner UserID
* `DATABASE_URL` - MongoDB Database URI for Saving UserID for Broadcast.
* `UPDATES_CHANNEL` - ID of a Channel which you want to do Force Sub to use the bot. *(Optional)*
* `LOG_CHANNEL` - Logs Channel ID for some Tracking.

### Deploy Now:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AbirHasan2005/PyroFilesStoreBot)

#### HOW TO DEPLOY

###### 1. Using the above deploy button if deploying on Heroku.
 - Click on it. Make sure you have all the creds ready.
 - Enter them in the fields provided, click deploy and wait for `Build Successful` message
 - Once it deploys successfully don't forget to **Turn on the Dyno** from `RESOURCES` tab.
 
###### 2. Manually deploying to Heroku (Import)
 - Import the repo and edit the config.py file and enter your creds if you know where to.
 - Heroku -> Create App -> Select it, goto `DEPLOY` tab and select GitHub and connect to your account by pressing the `LINK GITHUB ACCOUNT` button at the bottom.
 - Search for and select the imported repo and click deploy. Also, don't forget to **Turn on Dyno** from `RESOURCES` tab once it deploys successfully.

###### 3. Manually on Heroku (Fork, for lazy people without creds)
 - Fork this repo.
 - Create app on heroku. Open it and select `DEPLOY` tab and connect your GitHub account.
 - Search and select the imported repo and click deploy directly.
 - The repo will be deployed with dummy values in the Environment Variables. Doesn't matter as long as you don't turn on the dyno.
 - Whenever you are ready just edit the variables in `SETTINGS` -> `REVEAL CONFIG VARS`.
 - Turn on the dyno in `RESOURCES` tab once you enter all creds correctly.

###### 4. VPS.
 - Clone this repo with `git clone https://github.com/AbirHasan2005/PyroFilesStoreBot`
 - Change into the cloned repo `cd PyroFilesStoreBot`
 - Edit variables in config.py file with any text editor.(Remove dummy values and put your own). Vim: `vim config.py`
 - Run this command to install the prerequisites:`pip3 install -r requirements.txt` 
 - Lastly, run `python3 bot.py`(Linux) or `python bot.py`(Windows) to start the bot.
 
 
 


### Support Group:
<a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>

### Follow on:
<p align="left">
<a href="https://github.com/AbirHasan2005"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a>
</p>
<p align="left">
<a href="https://twitter.com/AbirHasan2005"><img src="https://img.shields.io/badge/Twitter-Follow%20on%20Twitter-informational.svg?logo=twitter"></a>
</p>
<p align="left">
<a href="https://facebook.com/AbirHasan2005"><img src="https://img.shields.io/badge/Facebook-Follow%20on%20Facebook-blue.svg?logo=facebook"></a>
</p>
<p align="left">
<a href="https://instagram.com/AbirHasan2005"><img src="https://img.shields.io/badge/Instagram-Follow%20on%20Instagram-important.svg?logo=instagram"></a>
</p>
