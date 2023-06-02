from aiogram import Bot, Dispatcher, executor, types
from text_to_qr import text_to_qr
import qrcode

TOKEN = "6161232627:AAHGXfRfqi9XJexB7m2HsIQZzXKm6X1BtiI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def start_handler(message: types.Message):
    await bot.send_photo(message.from_user.id, text_to_qr(message.text))


if __name__ == "__main__":
    executor.start_polling(dp)