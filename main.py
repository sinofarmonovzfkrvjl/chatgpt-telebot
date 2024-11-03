from telebot import TeleBot, types
import requests

API_TOKEN = "7596605488:AAFTbpv3_67TleOw8bm5JzSLqZCC0r9F4bY"

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