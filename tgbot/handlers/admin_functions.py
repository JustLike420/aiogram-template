import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline_all import mail_confirm_inl
from tgbot.data.loader import dp, bot
from tgbot.utils.misc.bot_filters import IsAdmin
from tgbot.utils.misc_functions import get_unix


@dp.message_handler(IsAdmin(), text="📢 Рассылка", state="*")
async def functions_mail(message: Message, state: FSMContext):
    await state.finish()

    await state.set_state("here_mail_text")
    await message.answer("<b>📢 Введите текст для рассылки пользователям</b>\n"
                         "❕ Вы можете использовать HTML разметку")


# РАССЫЛКА
@dp.message_handler(IsAdmin(), state="here_mail_text")
async def functions_mail_get(message: Message, state: FSMContext):
    await state.update_data(here_mail_text="📢 Рассылка.\n" + str(message.text))
    # TODO Функция получения всех пользователей из бд
    get_users = []

    cache_msg = await message.answer(message.text)
    await cache_msg.delete()

    await state.set_state("here_mail_confirm")
    await message.answer(
        f"<b>📢 Отправить <code>{len(get_users)}</code> юзерам сообщение?</b>\n"
        f"{message.text}",
        reply_markup=mail_confirm_inl,
        disable_web_page_preview=True
    )


@dp.callback_query_handler(IsAdmin(), text_startswith="confirm_mail", state="here_mail_confirm")
async def functions_mail_confirm(call: CallbackQuery, state: FSMContext):
    get_action = call.data.split(":")[1]

    send_message = (await state.get_data())['here_mail_text']
    # если много переменных
    #     async with state.proxy() as data:
    #         qiwi_login = data['here_qiwi_login']
    #         qiwi_token = data['here_qiwi_token']

    get_users = []
    await state.finish()

    if get_action == "yes":
        await call.message.edit_text(f"<b>📢 Рассылка началась... (0/{len(get_users)})</b>")
        asyncio.create_task(functions_mail_make(send_message, call))
    else:
        await call.message.edit_text("<b>📢 Вы отменили отправку рассылки ✅</b>")


async def functions_mail_make(message, call: CallbackQuery):
    receive_users, block_users, how_users = 0, 0, 0
    get_users = []
    get_time = get_unix()

    for user in get_users:
        try:
            await bot.send_message(user['user_id'], message, disable_web_page_preview=True)
            receive_users += 1
        except:
            block_users += 1

        how_users += 1

        if how_users % 10 == 0:
            await call.message.edit_text(f"<b>📢 Рассылка началась... ({how_users}/{len(get_users)})</b>")

        await asyncio.sleep(0.08)

    await call.message.edit_text(
        f"<b>📢 Рассылка была завершена за <code>{get_unix() - get_time}сек</code></b>\n"
        f"👤 Всего пользователей: <code>{len(get_users)}</code>\n"
        f"✅ Пользователей получило сообщение: <code>{receive_users}</code>\n"
        f"❌ Пользователей не получило сообщение: <code>{block_users}</code>"
    )
