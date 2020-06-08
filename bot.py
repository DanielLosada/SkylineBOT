# importa l'API de Telegram
import telegram
from telegram.ext import Updater, Filters
from telegram.ext import Updater, CommandHandler, MessageHandler
from skyline import Skyline
import pickle
from cl.EvalVisitor import EvalVisitor
import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser

skylines = {
    
}

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(update, context):
    botname = context.bot.username
    username = update.effective_chat.first_name
    missatge = "Hola %s, soc en %s" % (username, botname)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=missatge
        
    )

def help(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("Skyline.png", "rb")
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soc un bot amb comandes /start i /help.")

def author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Daniel Losada Molina. \n daniel.losada.molina@est.fib.upc.edu"
    )

def visitor(update, context):
    input_stream = InputStream(update.message.text)

    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()

    visitor = EvalVisitor()
    sky = visitor.visit(tree)
    sky.generarFigura()
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("Skyline.png", "rb")
    )
    sky.calculaAreaSkyline()
    sky.calculaAlçadaMax()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Àrea: " + str(sky.area)
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Alçada: " + str(sky.alcada)
    )

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(MessageHandler(Filters.text, visitor))



# engega el bot
updater.start_polling()


'''
import telegram
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler

#t.me/DanLMBOT

def start(bot, update): #(bot,callbackquery)
    botname = bot.username
    username = update.message.chat.first_name
    missatge = "Hola %s, soc en %s" % (username, botname)
    bot.send_message(chat_id=update.message.chat_id, text=missatge)
    print("Start command")


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soc un bot amb comandes /start, /help i /hora.")



TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))

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
'''
