from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext
from typing import Any

from tgbot.conversations import states


JSON = dict[str, Any]


def main_keyboard():
    return ReplyKeyboardMarkup([['Район', 'РСУ']], resize_keyboard=True)


def start(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    """Начало диалога, предложение выбрать поиск по району или РСУ"""
    update.message.reply_text('Район или РСУ?', reply_markup=main_keyboard())

    return states.CHOOSING
