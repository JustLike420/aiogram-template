from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageCantBeDeleted
from contextlib import suppress

from tgbot.data.loader import dp
from tgbot.keyboards.reply_all import main_menu


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
@dp.callback_query_handler(state="*")
async def main_missed_callback(call: CallbackQuery, state: FSMContext):
    with suppress(MessageCantBeDeleted):
        await call.message.delete()

    await call.message.answer("❌ Данные не были найдены из-за перезапуска скрипта.\n"
                              "♻ Выполните действие заново.",
                              reply_markup=main_menu(call.from_user.id))


# Обработка всех неизвестных команд
@dp.message_handler()
async def main_missed_message(message: Message):
    await message.answer("♦ Неизвестная команда.\n"
                         "▶ Введите /start")
