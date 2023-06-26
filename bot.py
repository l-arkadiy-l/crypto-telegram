from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from coins import *
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard_crypto = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)


@dp.message_handler(commands=['start'])
async def main(msg):
    await bot.send_message(msg.chat.id, 'hi, write which crypto rates you want see or /add crypto\nexample:\n/add bitcoin,dogecoin')


async def markup_reply():
    btn = KeyboardButton('hi')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btn)
    return keyboard


@dp.message_handler(commands=['add'])
async def user_input(msg):
    # add all crypto names
    # crypto can enter by ,
    # for example:
    # /add bitcoin,pepe,dogecoin
    crypto_names = [valid_coin.strip() for valid_coin in msg.text.split()[-1].split(',') if get_response(valid_coin.strip()).status_code == 200]
    keyboard_crypto.add(*crypto_names)
    await msg.reply(f'Added: {" and ".join(crypto_names)}', reply_markup=keyboard_crypto)


@dp.message_handler(content_types=['text'])
async def user_input(msg):
    coin = '-'.join(msg.text.split(' ')).lower()
    try:
        get_price(coin)
        photo = open(f'images/new.png', 'rb')
        await bot.send_photo(msg.chat.id, photo)
    except Exception:
        await msg.reply(f"Can't find {coin}")
    # await bot.delete_message(msg.chat.id, msg.message_id + 1)


executor.start_polling(dp)
