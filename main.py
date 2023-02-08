from aiogram import executor, Dispatcher

from tgbot.data.config import get_admins
from tgbot.middlewares import setup_middlewares
from tgbot.handlers import dp
from tgbot.utils.misc.bot_commands import set_commands
from tgbot.utils.misc_functions import on_startup_notify


async def on_startup(dp: Dispatcher):

    await set_commands(dp)
    await on_startup_notify(dp)
    # bot_logger.warning("BOT WAS STARTED")
    print("~~~~~ Bot was started ~~~~~")
    print("***** ENTER ADMIN ID *****") if len(get_admins()) == 0 else print(f"***** ADMINS: {len(get_admins())} *****")


if __name__ == '__main__':
    setup_middlewares(dp)
    executor.start_polling(dp, on_startup=on_startup)
