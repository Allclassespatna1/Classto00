import os

API_ID = API_ID = 21111175

API_HASH = os.environ.get("API_HASH", "fffea26a10b8c26ba900e1ed3d013d90")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7013832215:AAGUP5D7APrtiqpWy5d4VCsGMsnvFNSSDBA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6573766001,6381511858,5870116357))

LOG = -1002040082521

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6573766001,6381511858,5870116357").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


