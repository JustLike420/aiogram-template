import time

from aiogram import Dispatcher

from tgbot.data.config import get_admins
from tgbot.data.loader import bot


async def on_startup_notify(dp: Dispatcher):
    if len(get_admins()) >= 1:
        await send_admins(f"<b>✅ Бот был успешно запущен</b>")


# Рассылка сообщения всем администраторам
async def send_admins(message, markup=None, not_me=0):
    for admin in get_admins():
        # if markup == "default": markup = menu_frep(admin)

        try:
            if str(admin) != str(not_me):
                await bot.send_message(admin, message, reply_markup=markup, disable_web_page_preview=True)
        except:
            pass


# Получение текущего unix времени
def get_unix(full=False):
    if full:
        return time.time_ns()
    else:
        return int(time.time())
