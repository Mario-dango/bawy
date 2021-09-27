import telebot
from flask import flask, request
import os

API_TOKEN = '1733267643:AAEzJX64o3iQ9uHFGuZLig24tL6qYFvzeco'

bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Holiwis !")

@bot.message_handler(commands=['comand'])
def send_comands(message):
    bot.reply_to(message, "empty")

@server.router('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return "!", 200

@server.router("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://bawy.herokuapp.com/' + API_TOKEN)
    return "!", 200

if __name__ = "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

