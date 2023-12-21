import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

API_TOKEN = '6514287083:AAF92CBSMQKpVXJM2gXwgSIfu7a5hceK5O0'

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

obunachilar = []


@dp.message_handler(commands='start')
async def starter(message: Message):
    if message.from_user.id not in obunachilar:
        obunachilar.append(message.from_user.id)
    await message.answer("Assalomaleykum Bot ga xush kelibsiz!")


@dp.message_handler(text='reklama_admin')
async def rekalma(message: Message):
    if message.from_user.id == 5172746353:
        for i in obunachilar:
            with open("moshina.jpg", 'rb') as photo:
                await bot.send_photo(i, photo,
                                     caption="Yangi kuchuklar sotiladi arzon narxlarda Dastavchik Ibrohim")
    else:
        await message.answer("Siz admin emas siz")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
