import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '7626453968:AAGhkbuMlr4b1atnKRfyom7OpHyfIU6SKdg'
bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_menu = KeyboardButton('/menu')
    btn_whisper = KeyboardButton('/whisper')
    btn_scream = KeyboardButton('/scream')
    markup.add(btn_menu, btn_whisper, btn_scream)
    return markup
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "hola",
        reply_markup=main_menu()
    )
@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(
        message.chat.id,
        "Menu:\n/menu \n/whisper\n/scream",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['whisper'])
def whisper(message):
    bot.send_message(
        message.chat.id,
        "this is a whisper...",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['scream'])
def scream(message):
    bot.send_message(
        message.chat.id,
        "THIS IS A SCREAM!!!",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(
        message.chat.id,
        "SHO SHO???",
        reply_markup=main_menu()
    )

if __name__ == '__main__':
    print("Bot is running...")
    bot.polling()


