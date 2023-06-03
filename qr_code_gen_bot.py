import emoji
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup, ParseMode
# from aiogram.utils.emoji import emojize
import emoji
from aiogram.utils.markdown import text, pre

from text_to_qr import text_to_qr
import qrcode

TOKEN = "6161232627:AAHGXfRfqi9XJexB7m2HsIQZzXKm6X1BtiI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


button_qr = KeyboardButton('/text_to_qr')
button_kb = ReplyKeyboardMarkup()
button_kb.add(button_qr)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Hello! \n Welcome to our QR_Code to Text Bot \n To convert text into QR press /text_to_qr", reply_markup=button_kb)


@dp.message_handler(commands=['text_to_qr'])
async def start_handler(message: types.Message):
    tt = emoji.emojize("👇", use_aliases=True)
    await message.reply(f"Hello \nType your text {tt}")

    @dp.message_handler()
    async def text_to_qr_func(message: types.Message):
        await bot.send_photo(message.from_user.id, text_to_qr(message.text))
        await bot.send_message(message.from_user.id, "Type your next Text if you want!")

help_text = text(
                "This bot generates QR codes",
                "Commands: \n",
                "/start - Greeting",
                "/text_to_qr - Generate QR code", sep="\n"
)


@dp.message_handler(commands=["help"])
async def Help_function(message: types.Message):
    await bot.send_message(message.from_user.id, help_text)


if __name__ == "__main__":
    executor.start_polling(dp)