import os

API_ID = API_ID = 21537501

API_HASH = os.environ.get("API_HASH", "02d8ef0eae2926ec4fd0cbff05ec0737")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7251005777:AAHQ-qNJrZ1Wm683pu8-96pm6mqlTaBKxAc")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1485363731))

LOG = -1002223395843

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1485363731").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


