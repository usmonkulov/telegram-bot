import telebot

token = "5882263040:AAE3whJVXW9qp6ynHTLt-QcvHKYByIU0_7Q"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["id"])
def id(message):
    bot.send_message(message.chat.id, text="Id: " + str(message.chat.id) + "\n username: @" + str(message.from_user.username) + "\n your text: " + str(message.text) )


bot.polling(True)
