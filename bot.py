from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatType,Message,ContentType
API_TOKEN = '6580326658:AAFBYmlAhVhzAaevyKTW7D9a6YMYCiCMnlo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_bos(message:types.Message):
    await message.answer(f"Assalomu Aleykum {message.from_user.full_name}")
    await message.answer("👋🏻")

# @dp.message_handler(text='Sharifjon')
# async def sharifjon_uchun(message: types.Message):
#         await message.answer("Hi teacher!")
#         await message.answer("🫡")
#
# @dp.message_handler(text='Miralisher')
# async def miralisher_uchun(message: types.Message):
#         await message.answer("Hi Admin!")
#         await message.answer("🫡")

# @dp.message_handler(content_type =ContentType.TEXT)
# async def textga_javob_beradi(message:Message):
#     await message.answer("Siz text jo'natdingiz")
#
# @dp.message_handler(content_type =ContentType.VOICE)
# async def voicega_javob_beradi(message:Message):
#     await message.answer("Siz voice jo'natdingiz")


@dp.message_handler(content_types=[ContentType.VIDEO, ContentType.PHOTO])
async def videoga_javob_beradi(message: Message):
    await message.answer("Siz video yoki rasm jo'natdingiz")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)














# @dp.message_handler()
# async def startga_javob_beradi(message: types.Message):
#     print(message.from_user.is_premium)