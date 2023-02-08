from aiogram.types import ReplyKeyboardMarkup

from tgbot.data.config import get_admins


def main_menu(user_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("поле меню1", "поле меню2", "поле меню3")
    keyboard.row("поле меню4")
    if user_id in get_admins():
        keyboard.row("поле меню админа 1", "поле меню админа 2")
        keyboard.row("поле меню админа 3", "поле меню админа 4", "поле меню админа 5")
    return keyboard


def payments_repl():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🥝 Изменить QIWI 🖍", "🥝 Проверить QIWI ♻", "🥝 Баланс QIWI 👁")
    keyboard.row("⬅ Главное меню", "🖲 Способы пополнений")

    return keyboard


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
