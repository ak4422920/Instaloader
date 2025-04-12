# © Coded by @Dypixx

import os

API_ID = os.getenv("API_ID", "29171167")
API_HASH = os.getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", "7251898668"))

CHNL_LINK = os.getenv("CHNL_LINK", "https://t.me/Cineoriginals")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002264638393"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002264638393"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://tg:tg@cluster0.fekvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "cluster0")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002442422204") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH


"""
This code is created and owned by @Dypixx. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""
