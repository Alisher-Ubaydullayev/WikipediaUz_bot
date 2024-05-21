import wikipedia
from aiogram import types

from loader import dp

wikipedia.set_lang("uz")
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    try:
        resp = wikipedia.summary(message.text)
        await message.answer(resp)
    except:
        await message.answer("Bu mavzuga oid mavzu topilmadi")