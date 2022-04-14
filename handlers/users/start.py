import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        db.add_user(id=message.from_user.id, name=message.from_user.full_name)
    except sqlite3.IntegrityError as err:
        pass
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} botimizga xush kelibsiz !\n"
                         f"Botdan faydalanish bo'yicha yo'riqnoma bilan tanishib chiqing !\n"
                         f"/yordam")
    await bot.send_message(chat_id=ADMINS[0], text=f"{message.from_user.full_name} bazaga qo'shildi !")
