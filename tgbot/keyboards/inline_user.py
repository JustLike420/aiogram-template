from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as ikb


def some_user_func(some):
    keyboard = InlineKeyboardMarkup(

    ).add(
        ikb(text="test1", callback_data=f"show_purchases:{some}"),
        ikb(text="test2", callback_data=f"add_balance:{some}")
    ).add(
        ikb(text="test3", callback_data=f"skip_purchases:{some}"),
        ikb(text="test4", callback_data=f"delete_balance:{some}")
    )
    return keyboard
