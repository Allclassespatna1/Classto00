import os

API_ID = API_ID = 21111175

API_HASH = os.environ.get("API_HASH", "fffea26a10b8c26ba900e1ed3d013d90")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6770836525:AAGmRxvmxt2lR1pHJ-2owiq3aEg2tAGrGgo")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6834417723))

LOG = -4224442174

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6810033433").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


