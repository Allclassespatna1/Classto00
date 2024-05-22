import os

API_ID = API_ID = 21111175

API_HASH = os.environ.get("API_HASH", "fffea26a10b8c26ba900e1ed3d013d90")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7161485763:AAGEtR_zvt9FlZj0RLTq7l7Kg9-lX3-wn4A")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6810033433))

LOG = -1002086156755

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6810033433").split()):
        ADMINS.append(int("6573766001"))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


