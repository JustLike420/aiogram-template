# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup


# dynamic
def get_admin_func():
    functions_default = ReplyKeyboardMarkup(resize_keyboard=True)
    functions_default.row("📱 Поиск профиля 🔍", "📢 Рассылка", "📃 Поиск чеков 🔍")
    functions_default.row("⬅ На главную")
    return functions_default
