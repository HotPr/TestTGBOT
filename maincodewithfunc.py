import telebot



bot = telebot.TeleBot('5460370540:AAHw_PYPSD6zObQayMKk31N143DY_lyPx78')

@bot.message_handler(commands = ['start' , 'help'])
def start(message):
    nameuser = f'Привет, {message.from_user.first_name} {message.from_user.last_name}' 
    bot.send_message(message.chat.id, nameuser , parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')

bot.polling(non_stop=True)
