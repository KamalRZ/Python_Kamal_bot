import telebot, random, os, requests
import logic_bot
from logic_bot import bot
@bot.message_handler(commands=['hello'])
def c1(message):
    logic_bot.send_hello(message)
@bot.message_handler(commands=['heh'])
def c2(message):
    logic_bot.hehehehehe(message)
@bot.message_handler(commands=['bye'])
def c3(message):
    logic_bot.send_bye(message)
@bot.message_handler(commands=['mem'])
def c4(mess):
    logic_bot.send_mem(mess)
@bot.message_handler(commands=['duck'])
def c5(message):
    logic_bot.duck(message)
@bot.message_handler(commands=["ecolog"])
def c6(message):
    logic_bot.ecolog(message)
@bot.message_handler(commands=['help', 'start'])
def c7(message):
    logic_bot.send_welcome(message)


bot.infinity_polling()
