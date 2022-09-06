from cf_bot import dp, bot
from aiogram.utils import executor
from aiogram import types



@dp.message_handler(commands="start")
async def echo_sen(message : types.Message):
    await message.reply(f"Hi {message.from_user.first_name}. Я Эхобот, повторю любое отправленное сообщение)")


@dp.message_handler(content_types=['text'])
async def echo_message(message : types.Message):
    await bot.send_message(message.from_user.id, text=message.text)


executor.start_polling(dp)