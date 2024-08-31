from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def asosiyknopka():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text="Royxatdan o'tish")
    )
    return markup

