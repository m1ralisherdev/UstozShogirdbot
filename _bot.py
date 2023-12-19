import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

API_TOKEN = '6580326658:AAFBYmlAhVhzAaevyKTW7D9a6YMYCiCMnlo'

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

malumotlar = {

}  #


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
async def starter(message: Message, state: FSMContext):
    await message.answer(
        f"""Assalomu alaykum <b>{message.from_user.full_name}</b> ㅤㅤㅤㅤㅤㅤㅤㅤ
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""")
    await message.answer("<b>Ism, familiyangizni kiriting?</b>")
    await HELPERS.name_helper.set()


@dp.message_handler(state=HELPERS.name_helper)
async def name_taking(message: Message, state: FSMContext):
    name_surname = message.text
    malumotlar[message.from_user.id] = [name_surname]
    print(name_surname)
    await message.answer(
        "<b>📚 Texnologiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\nJava, C++, C#")
    await state.finish()
    await HELPERS.directon.set()


@dp.message_handler(state=HELPERS.directon)
async def direction_taking(message: Message, state: FSMContext):
    yonlaish = message.text
    malumotlar[message.from_user.id].append(yonlaish)
    a = yonlaish.replace(',', ' ')
    a = a.split()
    print(a)
    print(a)
    search = ''
    for i in a:
        search += f'#{i}  '
        print(search)
    malumotlar[message.from_user.id].append(search)

    await message.answer(
        "<b>🌐 Hudud:</b>\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.finish()
    await HELPERS.region.set()


@dp.message_handler(state=HELPERS.region)
async def region_taking(message: Message, state: FSMContext):
    region_2 = message.text
    malumotlar[message.from_user.id].append(region_2)
    print(region_2)
    await message.answer("<b>🕑 Yosh:</b>\n\nYoshingizni kiriting?\nMasalan, 19")
    await state.finish()
    await HELPERS.age.set()


@dp.message_handler(state=HELPERS.age)
async def age_taking(message: Message, state: FSMContext):
    age_2 = message.text
    malumotlar[message.from_user.id].append(age_2)
    print(age_2)
    await message.answer("<b>📞 Aloqa:</b> \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67")
    await state.finish()
    await HELPERS.number.set()


@dp.message_handler(state=HELPERS.number)
async def number_taking(message: Message, state: FSMContext):
    number_2 = message.text
    malumotlar[message.from_user.id].append(number_2)
    print(number_2)
    await message.answer("<b>💰 Narxi:</b>\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?")
    await state.finish()
    await HELPERS.price.set()


@dp.message_handler(state=HELPERS.price)
async def price_taking(message: Message, state: FSMContext):
    price_2 = message.text
    malumotlar[message.from_user.id].append(price_2)
    print(price_2)
    await message.answer("<b>👨🏻‍💻 Kasbi:</b> \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba")
    await state.finish()
    await HELPERS.job.set()


@dp.message_handler(state=HELPERS.job)
async def job_taking(message: Message, state: FSMContext):
    job_2 = message.text
    malumotlar[message.from_user.id].append(job_2)
    print(job_2)
    await message.answer(
        "<b>🕰 Murojaat qilish vaqti:</b>\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00")
    await state.finish()
    await HELPERS.time.set()

    @dp.message_handler(state=HELPERS.time)
    async def time_taking(message: Message, state: FSMContext):
        time_2 = message.text
        malumotlar[message.from_user.id].append(time_2)
        print(time_2)
        print(malumotlar)
        await message.answer(f"""
    Ma'lumotlarga ko'ra:

    👨‍💼 Xodim: <b>{malumotlar[message.from_user.id][0]}</b>
    🕑 Yosh: <b>{malumotlar[message.from_user.id][4]}</b>
    📚 Texnologiya: <b>{malumotlar[message.from_user.id][1]}</b>
    🇺🇿 Telegram: <b>@{message.from_user.username}</b>
    📞 Aloqa: <b>{malumotlar[message.from_user.id][5]}</b>
    🌐 Hudud: <b>{malumotlar[message.from_user.id][3]}</b>
    💰 Narxi: <b>{malumotlar[message.from_user.id][6]}</b>
    👨🏻‍💻 Kasbi: <b>{malumotlar[message.from_user.id][7]}</b>
    🕰 Murojaat qilish vaqti: <b>{malumotlar[message.from_user.id][8]}


    {malumotlar[message.from_user.id][2]}
    </b>""")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
