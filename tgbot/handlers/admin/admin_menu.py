from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline_admin import admin_menu_keyboard
from tgbot.utils.callback_data.admin import AdminMenu

router = Router(name=__name__)


@router.callback_query(AdminMenu.filter())
async def admin_menu_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("🤖 Админ Панель")
    await call.message.edit_reply_markup(reply_markup=admin_menu_keyboard())
