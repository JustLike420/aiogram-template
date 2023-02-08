from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

test_inl = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton("✅ test", callback_data="confirm:yes"),
    InlineKeyboardButton("❌ test", callback_data="confirm:not")
)

# Рассылка
mail_confirm_inl = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton("✅ Отправить", callback_data="confirm_mail:yes"),
    InlineKeyboardButton("❌ Отменить", callback_data="confirm_mail:not")
)

profile_open_inl = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton("💰 Пополнить", callback_data="user_refill"),
    InlineKeyboardButton("🎁 Мои покупки", callback_data="user_history")
)