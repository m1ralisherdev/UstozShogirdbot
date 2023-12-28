# default buttons bu past da chiqadigan tugmachalar
# ReplyKeyboardMarkup bu tugmachalarni yig`ib beradigan konteyner
# KeyboardButton yenngi tugmacha yaratish kodi


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧑‍🎓 Профиль'),
            KeyboardButton(text='🪙 Мои монеты'),
            KeyboardButton(text='💥 Space Shop')
        ],
        [
            KeyboardButton('🏫 О школе'),
            KeyboardButton('✍️ Оставить отзыв')
        ]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)
