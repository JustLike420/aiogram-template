from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from database.db import add_user
from tgbot.keyboards.reply_all import main_menu
from tgbot.data.loader import dp


@dp.message_handler(text=['⬅ Главное меню', '/start'], state="*")
async def main_start(message: Message, state: FSMContext):
    await state.finish()
    add_user(message)
    await message.answer("🔸 Бот готов к использованию.\n"
                         "🔸 Если не появились вспомогательные кнопки\n"
                         "▶ Введите /start",
                         reply_markup=main_menu(message.from_user.id))
