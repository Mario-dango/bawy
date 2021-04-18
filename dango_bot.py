#!/usr/bin/python

import telebot
import pyttsx3

API_TOKEN = '1763486620:AAEygw15xnK5-Tdni7sLJOK5JQ3z-Djgiok'

Dango = telebot.TeleBot(API_TOKEN)

###################################### Speak part engine
engine  = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Iniciando el bot de telegram..")



user = Dango.get_me()
print(user)
print("\n")
update = Dango.get_updates()
print(update)

# Handle '/start' and '/help'
@Dango.message_handler(commands=['help', 'start'])
def send_welcome(message):
    Dango.reply_to(message, """\
Holiwis yo soy DangoBot... etoou... también puedes llamarme solo dango hehe.
Pues.. mi amo (@niker_up) me ha creado para ser un asistente domótico y estaré en cosntante modificación, espero dar lo mejor de mí n.n\
""")
    #sti = open('C:/Users/mario/Documents/Telegram-bot/Dango_bot/files/stickers/hello.webp', 'rb')
    #Dango.send_sticker(message.chat.id, sti)


#def sendSticker(message):
#    # sendSticker
#    sti = open('/files/stickers/aww.webp', 'rb')
#    tb.send_sticker(chat_id, sti)
#    tb.send_sticker(chat_id, "FILEID")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@Dango.message_handler(func=lambda message: True)
def echo_message(message):
    
    print(message)
    print("\n")
    if (message.text.upper().find("hola") > 0):
        Dango.send_message(message.chat.id, "Hola señor")        
        sti = open('C:/Users/mario/Documents/Telegram-bot/Dango_bot/files/stickers/hug.webp', 'rb')
        Dango.send_sticker(message.chat.id, sti)
    #elif (message.text.upper().find(":(") < 0):
    Dango.reply_to(message, message.text)
    #    sti = open('C:/Users/mario/Documents/Telegram-bot/Dango_bot/files/stickers/aww.webp', 'rb')
    #    Dango.send_sticker(message.chat.id, sti)
    #elif (message.text.upper().find("Dango") > 0):
    #    Dango.send_message(message.chat.id, "Respecto a mi amo Dango lo único que puedo decir es que le debo mucho y lo quiero n.n")
    #    sti = open('C:/Users/mario/Documents/Telegram-bot/Dango_bot/files/stickers/aww.webp', 'rb')
    #    Dango.send_sticker(message.chat.id, sti)

Dango.polling()