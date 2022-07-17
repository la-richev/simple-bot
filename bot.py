import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# echo / works like a parrot
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

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