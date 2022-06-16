import telebot
from telebot import types
import requests

bot = telebot.TeleBot("", parse_mode=None)
bot.remove_webhook()

@bot.message_handler(commands=['civilizations'])
def dcivilizations(message):
    strlin=''
    i=0
    r=requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations').json()
    while i !=len(r['civilizations']):
        strlin=strlin+' Name:'+r['civilizations'][i]['name']+'\n Expansion:'+r['civilizations'][i]['expansion']+'\n Army_type:'+r['civilizations'][i]['army_type']+'\n'
        i += 1
    bot.send_message(message.chat.id, strlin)

@bot.message_handler(commands=['units'])
def dunits(message):
    strlin=''
    i=0
    r=requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/units').json()
    while i !=len(r['units']):
        strlin=strlin+' Name:'+r['units'][i]['name']+' Description:'+r['units'][i]['description']+' Expansion:'+r['units'][i]['expansion']+' Age:'+r['units'][i]['age']+' Hit_points:'+str(r['units'][i]['hit_points'])+'\n\n'
        i += 1
    bot.send_message(message.chat.id, strlin)

if __name__ == '__main__':
    bot.infinity_polling()