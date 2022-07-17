import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# # echo / works like a parrot
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

# start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ твой персональный AI-помощник Mera!")

# help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Если я плохо себя веду, напиши @richev он все исправит!")

# simple profanity check :3
@dp.message_handler()
async def filter_messages(message: types.Message):
    if 'плохое слово' in message.text:
        # profanity detected, remove
        await message.delete()

# remove new user joined messages
@dp.message_handler(content_types=['new_chat_members'])
async def on_user_joined(message: types.Message):
    await message.delete()

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)