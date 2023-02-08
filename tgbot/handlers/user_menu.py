from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.inline_all import profile_open_inl
from tgbot.data.loader import dp


@dp.message_handler(text="👤 Профиль", state="*")
async def user_profile(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("<b>Профиль</b>", reply_markup=profile_open_inl)
