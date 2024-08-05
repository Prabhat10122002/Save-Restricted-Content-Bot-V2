# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29815900"))
API_HASH = getenv("API_HASH", "5cc2ba67d33f00b22d697d2e04e29975")
BOT_TOKEN = getenv("BOT_TOKEN", "7403251612:AAE-ksjoOeopUWbN93MgTl7bgrJDZC8VyRI")
OWNER_ID = int(getenv("OWNER_ID", "1198391218"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://prabhatsingh10122002:dK4gc4vljnnloIX3@cluster0.0rysthe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002163104938"))
FORCESUB = getenv("FORCESUB", "https://t.me/pb_preperation")
