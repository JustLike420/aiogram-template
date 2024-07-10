from aiogram.utils.keyboard import ReplyKeyboardBuilder


def cancel_input_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Отменить ввод')
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)
