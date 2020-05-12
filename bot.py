import telegram
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler


def start(bot, update): #(bot,callbackquery)
    botname = bot.username
    username = update.message.chat.first_name
    missatge = "Hola %s, soc en %s" % (username, botname)
    bot.send_message(chat_id=update.message.chat_id, text=missatge)
    print("Start command")


TOKEN = open('token.txt').read().strip()

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
#dispatcher.add_handler(CommandHandler('help', help))
#dispatcher.add_handler(CommandHandler('author', author))
#dispatcher.add_handler(CommandHandler('lst', lst))
#dispatcher.add_handler(CommandHandler('clean', clean))
#dispatcher.add_handler(CommandHandler('save id', saveId))
#dispatcher.add_handler(CommandHandler('load id', loadId))

#dispatcher.add_handler(
#    MessageHandler(
 #       getLocation
#        ))

updater.start_polling()