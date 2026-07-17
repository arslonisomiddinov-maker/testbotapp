import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# BotFather'dan olgan maxfiy tokeningizni aniq shu qo'shtirnoq ichiga yozing
TOKEN = "8892755165:AAGx7WzsHRFZEa3FUVdxfcRndm96NZVfz8c"

# GitHub Pages sayt havolangiz
WEB_APP_URL = "https://arslonisomiddinov-maker.github.io/testbotapp/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Testni boshlash", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    
    await message.answer(
        f"Salom, {message.from_user.full_name}!\n\n"
        "Test tizimimizga xush kelibsiz. Testni boshlash uchun pastdagi tugmani bosing 👇",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
