from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.data.loader import dp
from tgbot.keyboards.reply_all import payments_repl
from tgbot.utils.misc.bot_filters import IsAdmin


@dp.message_handler(IsAdmin(), text="🔑 Платежные системы", state="*")
async def admin_payment(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("<b>🔑 Настройка платежных системы.</b>", reply_markup=payments_repl())