from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from ..utils.callback_data.admin import AdminTest
from ..utils.callback_data.user import MainMenu


def admin_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🔎 Поиск пользователя", callback_data=AdminTest())
    keyboard.button(text="⬅️ Назад", callback_data=MainMenu())
    keyboard.adjust(1)
    return keyboard.as_markup()

# def admin_menu_keyboard() -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardBuilder()
#
#     keyboard.row(
#         InlineKeyboardButton(text="🔎 Поиск пользователя", callback_data=GetAdminUser()),
#         InlineKeyboardButton(text="✉️ Создать рассылку", callback_data=AdminCreateNewsletter())
#     ).row(
#         InlineKeyboardButton(text="📅 Мероприятия", callback_data=AdminEvent())
#     ).row(
#         InlineKeyboardButton(text="⬅️ Назад", callback_data=MainMenu())
#     )
#
#     return keyboard.as_markup()
