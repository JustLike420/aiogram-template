from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.database.queries import get_user, add_user
from tgbot.keyboards.inline_user import menu_keyboard
from tgbot.utils.callback_data.user import MainMenu

router = Router(name=__name__)


@router.message(CommandStart())
async def main_start(message: Message, state: FSMContext):
    await state.clear()
    user = message.from_user
    db_user = await get_user(user_id=user.id)
    if not db_user:
        await add_user({
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username
        })
    await message.answer("🔸 Бот готов к использованию.\n", reply_markup=menu_keyboard(message.from_user.id))


@router.callback_query(MainMenu.filter())
async def main_menu_handler(call: CallbackQuery):
    await call.message.edit_text("Меню")
    await call.message.edit_reply_markup(reply_markup=menu_keyboard(call.from_user.id))
