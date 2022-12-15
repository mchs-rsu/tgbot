from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from tgbot.conversations import states
from tgbot.conversations.core import JSON
from tgbot.conversations.core import main_keyboard
from tgbot.conversations.api import client as api


def siren_choise(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    question = 'Какая РСУ интересует?'
    context.user_data['choice'] = 'siren'
    update.message.reply_text(question, reply_markup=ReplyKeyboardRemove())

    return states.SIREN_STATS


def siren_stats(update: Update, context: CallbackContext[JSON, JSON, JSON]) -> int:
    if not isinstance(update.message.text, str):
        update.message.reply_text('Введите текст')
        return states.SIREN_STATS

    target_sirens = update.message.text
    sirens = api.sirens.get_siren(target_sirens)

    if not sirens:
        update.message.reply_text('Такой РСУ в базе нет.')
        return states.SIREN_STATS

    if len(sirens) > 1:
        update.message.reply_text('Уточните, какая из этих РСУ нужна:')
        siren_name = [siren.name for siren in sirens]
        update.message.reply_text(', '.join(siren_name))
        return states.SIREN_STATS

    siren = sirens[0]
    district = api.districts.get_by_id(siren.district_id)

    answer = (
        f'<b>РСУ: {siren.name}</b> \n'
        f'Район: {district.name} \n'
        f'Тип: {siren.type} \n'
        f'Принадлежность: {siren.own} \n'
        f'Инженер: {siren.engineer} \n'
        f'Последний объезд: {siren.date} \n'
        f'Состояние: {siren.condition} \n'
        f'Идентификатор: {siren.ident} \n'
        f'IP: {siren.ip} \n'
        f'Маска: {siren.mask} \n'
        f'Шлюз: {siren.gateway} \n'
        f'Адрес: {siren.adress} \n'
        f'Координаты: {siren.geo} \n'
        f'Комментарий: {siren.comment}'
    )

    update.message.reply_html(answer)

    return states.CHOOSING
