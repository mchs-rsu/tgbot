from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from tgbot.conversations import states
from tgbot.conversations.core import JSON
from tgbot.conversations.core import main_keyboard
from tgbot.conversations.api import client as api


def district_choise(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    question = 'В каком районе нужно найти РСУ?'
    context.user_data['choice'] = 'district'
    update.message.reply_text(question, reply_markup=ReplyKeyboardRemove())

    return states.DISTRICT_STATS


def district_stats(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    if not isinstance(update.message.text, str):
        update.message.reply_text('Input text')
        return states.DISTRICT_STATS

    selected_district = update.message.text
    districts = api.districts.get_by_name(selected_district)

    if not districts:
        update.message.reply_text('В Татарстане нет такого района, проверьте правильность ввода')
        return states.DISTRICT_STATS

    district = districts[0]
    district_sirens = api.districts.get_for_district(district.uid)

    update.message.reply_text(f'{district.name} район:')
    siren_name = [siren.name for siren in district_sirens]
    update.message.reply_text(', '.join(siren_name))
    context.user_data['district_id'] = district.uid

    return states.SIREN_STATS
