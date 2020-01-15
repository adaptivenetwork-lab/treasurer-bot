import config
import handler
import gsheet
from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    start_handler = CommandHandler('start', handler.start)
    dp.add_handler(start_handler)

    kas_handler = CommandHandler('kas', handler.kas)
    dp.add_handler(kas_handler)
    
    updater.start_polling()

if __name__ == '__main__':
	main()