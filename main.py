import telebot

token = "5882263040:AAE3whJVXW9qp6ynHTLt-QcvHKYByIU0_7Q"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum")


bot.polling()
