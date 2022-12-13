from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler

from tgbot.conversations import states
from tgbot.conversations.core import start, cancel
from tgbot.conversations.districts import district_choise
from tgbot.conversations.sirens import siren_choise


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        states.CHOOSING: [
            MessageHandler(
                Filters.regex('^(District|Район)$'), district_choise,
            ),
            MessageHandler(
                Filters.regex('^(Siren|РСУ)$'), siren_choise,
            ),
        ],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
