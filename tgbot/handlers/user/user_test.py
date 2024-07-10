from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline_user import menu_keyboard
from tgbot.keyboards.reply_all import cancel_input_keyboard
from tgbot.utils.callback_data.user import Test
from tgbot.utils.states import TestState

router = Router(name=__name__)


@router.callback_query(Test.filter())
async def test_handler(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("введи текст", reply_markup=cancel_input_keyboard())
    await state.set_state(TestState.text)


@router.message(TestState.text)
async def get_text_handler(message: Message, state: FSMContext):
    text = message.text
    await state.clear()
    await message.answer(f"Ты ввел {text}")
    await message.answer(f"Меню", reply_markup=menu_keyboard(message.from_user.id))
