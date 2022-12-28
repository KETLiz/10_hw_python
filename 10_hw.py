import json
import requests
import telebot

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
dollar = response['Valute']["USD"]['Value']
euro = response['Valute']["EUR"]['Value']
print(euro)

bot = telebot.TeleBot("5810646799:AAFn9sMDTJJJXQucWKnPgRYg35uqNbt5Xng")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Выберите валюту: USD или EUR")

@bot.message_handler(content_types=['text'])
def currency(message):
    if message.text == 'USD':
        bot.send_message(message.chat.id, dollar)
    elif message.text == 'EUR':
        bot.send_message(message.chat.id, euro)

bot.infinity_polling()