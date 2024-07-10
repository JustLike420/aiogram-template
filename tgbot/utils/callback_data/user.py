from aiogram.filters.callback_data import CallbackData


class MainMenu(CallbackData, prefix='menu'):
    pass


class Test(CallbackData, prefix='test'):
    pass
