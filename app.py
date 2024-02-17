import telebot


bot = telebot.TeleBot('6354700436:AAEYcMduh7-_qOsEblGugiW7ZZX2f9E1pI8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Salem')






@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Jardem xizmeti ! Admin Kalli')


bot.polling(none_stop=True)