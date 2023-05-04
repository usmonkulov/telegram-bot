import telebot

token = "5882263040:AAE3whJVXW9qp6ynHTLt-QcvHKYByIU0_7Q"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["id"])
def id(message):
    cht = message.chat.id
    frt = message.chat.first_name
    usr = message.from_user.username
    typ = message.chat.type
    dat = message.date

    bot.send_message(message.chat.id,
                     text="ID : {}\nName : {}\nUser : @{}\nType : {}\nDate Msg : {}\nChannel : [Bobur Usmonkulov | Dev](t.me/bobur_usmonkulov_blog)".format(
                         cht, frt, usr, typ, dat), disable_web_page_preview="true")


@bot.message_handler(regexp="^id")
def reply(message):
    if message.reply_to_message:
        id = message.reply_to_message.from_user.id
        bot.send_message(message.chat.id, id)


bot.polling(True)
