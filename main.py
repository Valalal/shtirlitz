rom bs4 import BeautifulSoup as b
import requests
import random
import telebot

url = 'https://www.anekdot.ru/tags/%D0%A8%D1%82%D0%B8%D1%80%D0%BB%D0%B8%D1%86'

token_tele = '5508847230:AAEHGIrn1sSVKz4y0XZ8YGBcPY30Z0kiRDQ'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anecdot = soup.find_all('div', class_='text')
    return [c.text for c in anecdot]


list_of_anecdot = parser(url)

random.shuffle(list_of_anecdot)

bot = telebot.TeleBot(token_tele)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Сколько раз постучать в дверь?')


@bot.message_handler(content_types=['text'])
def joke(message):
    if message.text.lower().isdigit() == True:
        if int(message.text.lower()) == 300:
            bot.send_message(message.chat.id, 'сам знаешь, что сделать с трактористом')
        if int(message.text.lower()) == 0:
            bot.send_message(message.chat.id, 'дырка от бублика тебе, а не анекдот.')
            bot.send_message(message.chat.id, 'шучу.')
        bot.send_message(message.chat.id, list_of_anecdot[0])
        del list_of_anecdot[0]
    else:
        bot.send_message(message.chat.id, 'введи число')


bot.polling()
