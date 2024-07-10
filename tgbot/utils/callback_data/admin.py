from aiogram.filters.callback_data import CallbackData


class AdminMenu(CallbackData, prefix='admin_menu'):
    pass


class AdminTest(CallbackData, prefix='admin_test'):
    pass
