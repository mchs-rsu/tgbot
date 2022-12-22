from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext, ConversationHandler
from typing import Any

from tgbot.conversations import states


JSON = dict[str, Any]


def main_keyboard():
    return ReplyKeyboardMarkup([['Район', 'РСУ']], resize_keyboard=True)


def start(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Начало диалога, предложение выбрать поиск по району или РСУ"""

    question = 'Что интересует, район или РСУ?'
    update.message.reply_text(question, reply_markup=main_keyboard())

    return states.CHOOSING


def cancel(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    question = 'Bue!'
    update.message.reply_text(question)

    return ConversationHandler.END
