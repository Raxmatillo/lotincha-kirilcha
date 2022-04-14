from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.lotin_kiril import ToLatin, ToCyrilic, latin, cyrilic

from loader import dp


@dp.message_handler()
async def latin_cyril(message: types.Message):
    source_message = message.text
    sts = message.text[0]
    if sts in latin:
        to_cyril = ToCyrilic(source_message)
        await message.reply(to_cyril)
    elif sts in cyrilic:
        to_latin = ToLatin(source_message)
        await message.reply(to_latin)
    else:
        await message.reply("Iltimos, matn bilan boshlanuvchi so'z kiriting !!!")