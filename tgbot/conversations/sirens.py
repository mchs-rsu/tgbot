from telegram import Update
from telegram.ext import CallbackContext

from tgbot.conversations import states
from tgbot.conversations.core import JSON
from tgbot.conversations.core import main_keyboard


def siren_choise(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    question = 'Какая РСУ интересует?'
    context.user_data['choice'] = 'siren'
    update.message.reply_text(question, reply_markup=main_keyboard)

    return states.SIREN_STATS
