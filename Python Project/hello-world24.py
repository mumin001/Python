# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:44:22 2022

@author: User
"""

import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '5518842824:AAEftD6ZBEfJIBwwtxNjSoVEdo1Rxsb9baM'
bot = telebot.TeleBot(token=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = (
        message.from_user.username
    )
    javob = f"Assalomu alaykum,{username} Xush kilibsiz!"
    javob = "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda msg: msg.trxt is not None)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))    

bot.polling()    

# matn = input("Matn kiriting:")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))