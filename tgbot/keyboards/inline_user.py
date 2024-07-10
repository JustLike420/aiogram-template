from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..data.config import get_admins
from ..utils.callback_data.admin import AdminMenu
from ..utils.callback_data.user import Test


def menu_keyboard(user_id: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="тест", callback_data=Test())
    if user_id in get_admins():
        keyboard.button(text="Админ тест", callback_data=AdminMenu())
    return keyboard.as_markup()
