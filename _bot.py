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
    price = State()
    job = State()
    time = State()
    wants = State()
    info = State()
@dp.message_handler(commands='start')
async def starter(message: Message, state:FSMContext):
    await message.answer(f"Assalomu alaykum <b>{message.from_user.full_name}</b>\nZAM AGENCY kanalining rasmiy botiga xush kelibsiz!")
    await message.answer("Ariza qoldirish uchun ismingizni kiriting")
    await HELPERS.name_helper.set()
@dp.message_handler(state=HELPERS.name_helper)
async def name_taking(message: Message, state:FSMContext):
    name_surname = message.text
    print(name_surname)
    await message.answer("<b>📚 Texnologiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\nJava, C++, C#")
    await state.finish()
    await HELPERS.directon.set()
@dp.message_handler(state=HELPERS.directon)
async def direction_taking(message: Message, state:FSMContext):
    direction_2 = message.text
    a = direction_2.replace(',',' ')
    a = a.split()
    print(a)
    await message.answer("<b>🌐 Hudud:</b>\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.finish()
    await HELPERS.region.set()
@dp.message_handler(state=HELPERS.region)
async def region_taking(message: Message, state:FSMContext):
    region_2 = message.text
    print(region_2)
    await message.answer("<b>🕑 Yosh:</b>\n\nYoshingizni kiriting?\nMasalan, 19")
    await state.finish()
    await HELPERS.age.set()
@dp.message_handler(state=HELPERS.age)
async def age_taking(message: Message, state:FSMContext):
    age_2 = message.text
    print(age_2)
    await message.answer("<b>📞 Aloqa:</b> \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67")
    await state.finish()
    await HELPERS.number.set()
@dp.message_handler(state=HELPERS.number)
async def number_taking(message: Message, state:FSMContext):
    number_2 = message.text
    print(number_2)
    await message.answer("<b>💰 Narxi:</b>\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await state.finish()
    await HELPERS.price.set()
@dp.message_handler(state=HELPERS.price)
async def price_taking(message: Message, state:FSMContext):
    price_2 = message.text
    print(price_2)
    await message.answer("<b>👨🏻‍💻 Kasbi:</b> \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba")
    await state.finish()
    await HELPERS.job.set()

@dp.message_handler(state=HELPERS.job)
async def job_taking(message: Message, state:FSMContext):
    job_2 = message.text
    print(job_2)
    await message.answer("<b>🕰 Murojaat qilish vaqti:</b>\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await state.finish()
    await HELPERS.time.set()

@dp.message_handler(state=HELPERS.time)
async def time_taking(message: Message, state:FSMContext):
    time_2 = message.text
    print(time_2)
    await message.answer(f"Ma'lumotlarga ko'ra: \n\n👨‍💼 Xodim: <b></b>\n🕑 Yosh: <b></b>\n📚 Texnologiya: <b></b>\n🇺🇿 Telegram: <b>@{message.from_user.username}</b>\n📞 Aloqa: <b></b>\n🌐 Hudud: <b></b>\n💰 Narxi: <b></b>\n👨🏻‍💻 Kasbi: <b></b>\n🕰 Murojaat qilish vaqti: <b></b>")
#     await message.answer("This is a simple Telegram bot.\n\nAvailable commands:\n/start - Start the bot\n/help - Show this help message")
#     await state.finish()
#     await HELPERS.help
# @dp.message_handler(commands='help')
# async def help_command(message: Message, state:FSMContext):
#     help_text = message.text
#     await message.answer(help_text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
