import os

API_ID = API_ID = 21537501

API_HASH = os.environ.get("API_HASH", "02d8ef0eae2926ec4fd0cbff05ec0737")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6997850062:AAHWrgAFDhUqJZ_ymrJKxlH1N--HvjNcyxE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6573766001))

LOG = -1002040082521

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6573766001").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


