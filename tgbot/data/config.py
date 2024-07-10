from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')


def get_admins() -> list[int]:
    admins = os.getenv('ADMINS')
    admins = [admin.strip() for admin in admins.split(",")] if "," in admins else [admins] if admins else []
    admins = list(map(int, admins))
    return admins
