import telebot
from telebot.apihelper import send_message
from telebot.types import Chat, Message

from api_tg import api
token = api()
print()
API_TOKEN = token

bawy = telebot.TeleBot(API_TOKEN)
user = bawy.get_me()
print(user)
print("\n")
update = bawy.get_updates()
print(update)

# Handle '/start' and '/help'
@bawy.message_handler(commands=['help','start'])
def send_welcome(message):    
    bawy.reply_to(message, """\
Holiwis yo soy BawyBot... etoou... también puedes llamarme BB hehe.
Pues.. mi amo (@BawBaaw) me ha creado para ser un asistente domótico y estaré en cosntante modificación, espero dar lo mejor de mí n.n\
""")
    sti = open('C:/Users/mario/Documents/Telegram-bot/bawy_bot/files/stickers/hello.webp', 'rb')
    bawy.send_sticker(message.chat.id, sti)

# Handle '/start' and '/help'
@bawy.message_handler(commands=['tank'])
def send_welcome(message):    
    bawy.reply_to(message, """\
Oki Doki~\
""")
    sti = open('C:/Users/mario/Documents/Telegram-bot/bawy_bot/files/stickers/hello.webp', 'rb')
    bawy.send_sticker(message.chat.id, sti)



#def sendSticker(message):
#    # sendSticker
#    sti = open('/files/stickers/aww.webp', 'rb')
#    tb.send_sticker(chat_id, sti)
#    tb.send_sticker(chat_id, "FILEID")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bawy.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    print("\n")
    if (message.text.upper().find("ayer") > 0):
        bawy.send_message(message.chat.id, "Respecto a mi amo Bawy lo único que puedo decir es que le debo mucho y lo quiero n.n")
        sti = open('C:/Users/mario/Documents/Telegram-bot/bawy_bot/files/stickers/yes.webp', 'rb')
        bawy.send_sticker(message.chat.id, sti)
    elif (message.text.upper().find("(") > 0):
        bawy.send_message(message.chat.id, "No estes triste, la gente te quiere, yo te quiero! <3")
        sti = open('C:/Users/mario/Documents/Telegram-bot/bawy_bot/files/stickers/hug.webp', 'rb')
        bawy.send_sticker(message.chat.id, sti)
    elif (message.text.upper().find(":(") < 0):
        bawy.reply_to(message, message.text)
        sti = open('C:/Users/mario/Documents/Telegram-bot/bawy_bot/files/stickers/aww.webp', 'rb')
        bawy.send_sticker(message.chat.id, sti)


bawy.polling()