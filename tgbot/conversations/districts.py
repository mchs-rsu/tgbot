from telegram import Update
from telegram.ext import CallbackContext

from tgbot.conversations import states
from tgbot.conversations.core import JSON
from tgbot.conversations.core import main_keyboard


def district_choise(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    question = 'В каком районе нужно найти РСУ?'
    context.user_data['choice'] = 'district'
    update.message.reply_text(question, reply_markup=main_keyboard)

    return states.DISTRICT_STATS
