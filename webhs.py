import os
os.system("pip install telebot")
from telebot import TeleBot
from os import *

b = TeleBot("7041660971:AAFRHRd6xHhxDMZ8l8tSLKdmZCL88ulbmwE")

@b.message_handler(commands=['start'])

def s(m):
    system(f"mkdir user{m.chat.id}")
    system(f"mkdir user{m.chat.id}/Balance")
    b.send_message(m.chat.id, """
ㅤㅤ☄ Здраствуйте ☄ㅤㅤ
ㅤ/help - Помощь по игре
""")
   
@b.message_handler(commands=['help'])

def help(mm):
    b.send_message(mm.chat.id, """
ㅤㅤ✎ Помощь ✎ㅤㅤㅤㅤ
ㅤ/profile - Профильㅤㅤ
""")

@b.message_handler(commands=['profile'])

def profile(m):
        try:
            with open("r", f"user{m.chat.id}/Balance/balance.txt") as fl:
                fll = fl.read()
                b.send_message(m.chat.id, f"""
👤 Профиль:
    
💰 Баланс: {fll}₽""")
        except:
            b.send_message(m.chat.id, """
👤 Профиль:

💰 Баланс: 0₽ - кликов нету""")
            
b.infinity_polling(none_stop=True)
