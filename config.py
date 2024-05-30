import os

API_ID = API_ID = 21537501

API_HASH = os.environ.get("API_HASH", "02d8ef0eae2926ec4fd0cbff05ec0737")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7252678241:AAH_GtzPB3A9AV1RQ3qfv5mcFsS01dz3OZQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6573766001))

LOG = -4213604816

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "x").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


