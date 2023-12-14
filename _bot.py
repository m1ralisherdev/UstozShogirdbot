import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '6580326658:AAFBYmlAhVhzAaevyKTW7D9a6YMYCiCMnlo'

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class YORDAMCHILAR(StatesGroup):
    ism_yordamchisi = State()
    yonalish = State()
    hudud = State()


@dp.message_handler(commands='start')
async def starter(message: Message, state: FSMContext):
    await message.answer(f"Assalomu Aleykum <b>{message.from_user.full_name}</b>")
    await message.answer("Ariza qoldirish uchun ismingizni kiriting !")

    await YORDAMCHILAR.ism_yordamchisi.set()


@dp.message_handler(state=YORDAMCHILAR.ism_yordamchisi)
async def ism_qabul_qilib_ol(message: Message, state: FSMContext):
    ism_familiya = message.text
    print(ism_familiya)
    await message.answer("Yo`nalishingizni tanlang")
    await state.finish()
    await YORDAMCHILAR.yonalish.set()


@dp.message_handler(state=YORDAMCHILAR.yonalish)
async def yonalish_qabul_qilish(message: Message, state: FSMContext):
    yunalish = message.text
    print(yunalish)
    await message.answer("hududni tanlang ")
    await state.finish()
    await YORDAMCHILAR.hudud.set()


@dp.message_handler(state=YORDAMCHILAR.hudud)
async def hudud_tanglash(message: Message, state: FSMContext):
    hudud_boshqarish = message.text
    print(hudud_boshqarish)

#
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)