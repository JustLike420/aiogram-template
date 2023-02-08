from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.reply_all import main_menu
from tgbot.data.loader import dp


@dp.message_handler(text=['⬅ Главное меню', '/start'], state="*")
async def main_start(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("🔸 Бот готов к использованию.\n"
                         "🔸 Если не появились вспомогательные кнопки\n"
                         "▶ Введите /start",
                         reply_markup=main_menu(message.from_user.id))
