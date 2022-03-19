from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

sendd = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Tasdiqlash',callback_data="tasq"),InlineKeyboardButton(text = "Bekor qilish",callback_data="non")]
    ]
)

# send_ad = InlineKeyboardMarkup(
#     inline_keyboard = [
#         [InlineKeyboardButton(text = 'Tasdiqlash',callback_data="send_ch"),InlineKeyboardButton(text = "Bekor qilish",callback_data="cancel")]
#     ]
# )