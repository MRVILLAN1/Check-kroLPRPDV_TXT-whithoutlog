import os

API_ID = API_ID = 28837789

API_HASH = os.environ.get("API_HASH", "33c9162294cdd6c9d51d964e4469fadb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "7493"))

OWNER = int(os.environ.get("OWNER", 8087702564))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5684410709").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


