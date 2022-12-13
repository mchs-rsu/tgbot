from tgbot.conversations.core import main_keyboard
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler

from tgbot.conversations import states
from tgbot.conversations.core import start


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        states.CHOOSING: [
            MessageHandler(
                Filters.regex('^(District|Район)$'), city_choice,
            ),
            MessageHandler(
                Filters.regex('^(Siren|РСУ)$'), place_choice,
            ),
        ],
    }
)
