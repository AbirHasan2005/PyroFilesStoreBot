{
    "name": "Telegram Files Store Bot",
    "description": "A Telegram Files Store Bot in Pyrogram by @AbirHasan2005",
    "keywords": [
        "telegram",
        "files",
        "store",
        "bot"
    ],
    "repository": "https://github.com/AbirHasan2005/PyroFilesStoreBot",
    "website": "https://telegram.dog/AbirHasan2005",
    "success_url": "https://t.me/Discovery_Updates",
    "env": {
        "API_ID": {
            "description": "Get this value from my.telegram.org or @TeleORG_Bot"
        },
        "API_HASH": {
            "description": "Get this value from my.telegram.org or @TeleORG_Bot"
        },
        "BOT_TOKEN": {
            "description": "Get this from @BotFather XD"
        },
        "BOT_USERNAME": {
            "description": "Your Bot Username which you sent to @BotFather (Without [@])"
        },
        "DB_CHANNEL": {
            "description": "The Channel ID which will be used as Database. Example: -100123456789"
        },
        "BOT_OWNER": {
            "description": "Bot Owner UserID"
        },
        "DATABASE_URL": {
            "description": "MongoDB Database URI for Saving UserID for Broadcast."
        },
        "UPDATES_CHANNEL": {
            "description": "ID of a Channel which you want to do Force Sub to use the bot. Example: -100123456789",
            "required": false
        },
        "LOG_CHANNEL": {
            "description": "Logs Channel ID for some Tracking XD. Example: -100123456789"
        },
        "BANNED_USERS": {
            "description": "Banned unwanted members",
            "required": false
        },
        "BANNED_CHAT_IDS": {
            "description": "Banned unwanted channel IDs",
            "required": false
        },
        "BROADCAST_AS_COPY": {
            "description": "Broadcast with Forward Tag or as Copy(Without Forward Tag). Value should be True/False !!",
            "required": false
        },
        "FORWARD_AS_COPY": {
            "description": "If True all messages will be forwarder As Copy. If False all messages will be forwarder with Forward Tag. Value should be True/False !!",
            "required": false
        }
    },
    "buildpacks": [
        {
            "url": "heroku/python"
        }
    ],
    "formation": {
        "worker": {
            "quantity": 1,
            "size": "free"
        }
    }
}
