from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


send_ad = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Tasdiqlash',callback_data="send_ch"),InlineKeyboardButton(text = "Bekor qilish",callback_data="cancel")]
    ]
)