from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')
PATH_DATABASE = os.getenv('PATH_DATABASE')


def get_admins() -> list:
    ADMINS = os.getenv('ADMINS')
    admins = [admin.strip() for admin in ADMINS.split(",")] if "," in ADMINS else [ADMINS] if ADMINS else []
    return admins
