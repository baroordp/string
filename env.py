import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "20822386").strip()
API_HASH = os.getenv("API_HASH", "4f0069e749e20d9c399447b4a34f5a45").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7627762738:AAH-FRVhGkP0R06AkRcKIuDK5OhbcItAc6k").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://sk3:sk3@cluster0.7jowr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "-1002450276019")
PORT = os.getenv("PORT", "8080")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
