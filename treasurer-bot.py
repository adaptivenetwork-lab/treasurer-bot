from telegram.ext import Updater, CommandHandler
import logging

updater = Updater(token='1032606426:AAE2fXbgpOc2N7dY7kURt__jCWC0KedTQZY', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                    text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()