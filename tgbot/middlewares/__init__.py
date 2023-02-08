from aiogram import Dispatcher

from tgbot.middlewares.throttling import ThrottlingMiddleware


# Подключение милдварей
def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
