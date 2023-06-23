import telebot
from coins import *
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(msg):
    bot.send_message(msg.chat.id, 'hi, write which crypto rates you want see')


@bot.message_handler(content_types=['text'])
def user_input(msg):
    coin = '-'.join(msg.text.split(' '))
    try:
        bot.send_message(msg.chat.id, f'Waiting... I am finding this coin')
        get_price(coin)
        bot.delete_message(msg.chat.id, msg.message_id + 1)
        bot.send_photo(msg.chat.id, photo=open('images/new.png', 'rb'))
    except Exception:
        bot.send_message(msg.chat.id, f'Try again! We dont find {coin}')


bot.polling(none_stop=True)
