from telebot import TeleBot, types
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("TOKEN")

bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Salom, {message.from_user.first_name}\nmen sizning AI yordamchingizman")

@bot.message_handler(func=lambda message: True)
def chatgpt(message: types.Message):
    response = requests.get("http://cybergenius.uz/v1_api/chat_gpt/main.php?savol=" + message.text)
    bot.send_message(message.chat.id, response.json()['message'])


print(f"[@{bot.get_me().username}] - {bot.get_me().full_name}")
bot.infinity_polling(skip_pending=True)