#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6126068979:AAH0wtssU8xhORW_5AoiD8n5RWN9aFevCb4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "17474742"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3a4df9f349ffe0a32d07c23d7f5b4a03")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001557692189"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5493260414"))

#Port
PORT = os.environ.get("PORT", "8040")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://AnimeUniverseBot:Kaizo007@cluster0.rzzh05o.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001872656213"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001553006202"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first} 👋\n\nI am  a file store bot for @anime_channelz, please join the channel to use me</b>.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1690217497").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(5984303934)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
