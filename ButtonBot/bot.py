import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
import openpyxl
from openpyxl import Workbook
import datetime

# Bot initialization
API_TOKEN = '6580326658:AAG3oFYRU-FeqxoqHn0-_MluEWKaceT8eao'
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
from buttons import start_button


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer('Assalomu Aleykum', reply_markup=start_button)


@dp.message_handler(text='🧑‍🎓 Профиль')
async def mening_profilim(message: types.Message):
    await message.reply("""
Ism: Mirmahmudov
Familiya: Miralisher
Til: uz
Ta’lim markazi: YUNUSABAD
""")


#

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
