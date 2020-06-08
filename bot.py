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

    visitor = EvalVisitor(context.user_data)
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
        text = "Àrea: " + str(sky.area) + '\n' + "Alçada: " + str(sky.alcada)
    )
    

def save(update, context):
    arg = str(context.args[0])
    idSky = context.user_data[arg]
    nomfile = arg + '.sky'
    fi = open(nomfile, 'wb')
    pickle.dump(idSky, fi)
    fi.close()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Skyline guardat!"
    )

def load(update, context):
    arg = str(context.args[0])
    nomfile = arg + '.sky'
    fi = open(nomfile, 'rb')
    var = pickle.load(fi)
    context.user_data[arg] = var
    fi.close()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Skyline carregat!"
    )

def clean(update, context):
    context.user_data.clear()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = "Identificadors esborrats!"
    )

def lst(update,context):
    keysDic = context.user_data.keys()
    for x in keysDic:
        missatge = 'Identificador: ' + str(x) + '   Àrea: ' + str(context.user_data[str(x)].area)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = missatge
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
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(MessageHandler(Filters.text, visitor))



# engega el bot
updater.start_polling()
