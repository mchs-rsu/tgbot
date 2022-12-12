import logging
import os

from telegram.ext import Updater, CommandHandler


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Район или РСУ?')


def main():
    logger.info('hello')
    updater = Updater(os.environ['TOKEN'])

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', greet_user))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
