# import logging
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import Message
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ParseMode
# import openpyxl
# from openpyxl import Workbook
# import datetime
#
# # Bot initialization
# API_TOKEN = '6580326658:AAG3oFYRU-FeqxoqHn0-_MluEWKaceT8eao'
# bot = Bot(token=API_TOKEN, parse_mode='HTML')
# dp = Dispatcher(bot, storage=MemoryStorage())
# logging.basicConfig(level=logging.INFO)
#
# # Excel initialization
# wb = Workbook()
# ws = wb.active
# wb_read = openpyxl.load_workbook('database.xlsx')
# sheet = wb_read.active
#
# barcha_idlar_soni = sheet.max_row
#
# odamlar = []
# vaqtlar = []
#
# # Load existing user data
# for i in range(1, barcha_idlar_soni + 1):
#     id_telegram = sheet.cell(row=i, column=1).value
#     if id_telegram:
#         odamlar.append(int(id_telegram))
#
#     vaqt_qoshilgan = sheet.cell(row=i, column=2).value
#     if vaqt_qoshilgan:
#         vaqtlar.append(vaqt_qoshilgan)
#
#
# # Dispatcher
# @dp.message_handler(commands='start')
# async def starter(message: Message):
#     x = datetime.datetime.now()
#     now = f"{x.strftime('%d')}/{x.strftime('%X')}"
# #
#     if message.from_user.id not in odamlar:
#         odamlar.append(message.from_user.id)
#         vaqtlar.append(now)
#
#         for i in range(1, len(odamlar) + 1):
#             ws[f'A{i}'] = odamlar[i - 1]
#             if vaqtlar[i - 1].startswith(x.strftime('%d')):
#                 ws[f'A{i}'].font = openpyxl.styles.Font(color="00FF00")
#             else:
#                 ws[f'A{i}'].font = openpyxl.styles.Font(color="FF0000")  #
#
#             ws[f'B{i}'] = vaqtlar[i - 1]
#
#         wb.save('database.xlsx')
#         await message.answer("Assalomaleykum Bot ga xush kelibsiz!\nSiz uchun bonuslarimiz mavjud")
#
#     else:
#         await message.answer(
#             "Assalomaleykum! Siz botdan oldin ro`yxatdan o`tib bo`lgansiz. Siz uchun bonuslar mavjud emas!")
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
