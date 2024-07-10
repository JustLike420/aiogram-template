from aiogram import Dispatcher

from tgbot.handlers.admin import admin_menu
from tgbot.handlers.user import main_start, user_test


def register_all_routers(dp: Dispatcher):
    admin_menu.router.message.filter()

    dp.include_router(admin_menu.router)
    dp.include_router(main_start.router)
    dp.include_router(user_test.router)
