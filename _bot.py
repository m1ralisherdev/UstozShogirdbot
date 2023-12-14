import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message,ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

API_TOKEN = '6304492965:AAFe9wqA17pgLwtMZPW23DZImQtP3kWWCJc'

bot = Bot(token=API_TOKEN,parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

class HELPERS(StatesGroup):
    name_helper = State()
    directon = State()
    region = State()
    age = State()
    number = State()
    help = State()

@dp.message_handler(commands='start')
async def starter(message: Message, state:FSMContext):
    await message.answer(f"Assalomu alaykum <b>{message.from_user.full_name}</b>")
    await message.answer("Ariza qoldirish uchun ismingizni kiriting")
    await HELPERS.name_helper.set()
@dp.message_handler(state=HELPERS.name_helper)
async def name_taking(message: Message, state:FSMContext):
    name_surname = message.text
    print(name_surname)
    await message.answer("Yo'nalishingizni tanlang 💼")
    await state.finish()
    await HELPERS.directon.set()
@dp.message_handler(state=HELPERS.directon)
async def direction_taking(message: Message, state:FSMContext):
    direction_2 = message.text
    print(direction_2)
    await message.answer("Hududingizni tanlang 🌍")
    await state.finish()
    await HELPERS.region.set()
@dp.message_handler(state=HELPERS.region)
async def region_taking(message: Message, state:FSMContext):
    region_2 = message.text
    print(region_2)
    await message.answer("Yoshingizni kiriting")
    await state.finish()
    await HELPERS.age.set()
@dp.message_handler(state=HELPERS.age)
async def age_taking(message: Message, state:FSMContext):
    age_2 = message.text
    print(age_2)
    await message.answer("Telefon raqamingizni kiriting 📞")
    await state.finish()
    await HELPERS.number.set()
@dp.message_handler(state=HELPERS.number)
async def number_taking(message: Message, state:FSMContext):
    number_2 = message.text
    print(number_2)
    await message.answer("This is a simple Telegram bot.\n\nAvailable commands:\n/start - Start the bot\n/help - Show this help message")
    await state.finish()
    await HELPERS.help
@dp.message_handler(commands='help')
async def help_command(message: Message, state:FSMContext):
    help_text = message.text
    await message.answer(help_text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
