
# -*- coding: utf-8 -*-

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ��� ����� ����
bot_token = '6788095013:AAGGA7ckQLqp-D_cZKKdsY3QcpM-FKyOsls'
# ID ������ ��� ������������, ���� ����� ������������ ���������
user_id = '-1002120118788'

# �������������� ������� ��������
question_counter = 76

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Добро пожаловать в бота, где вы сможете отправлять анонимные вопросы, идеи или предложения. Пишите сюда ваш вопрос:')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global question_counter
    message_text = update.message.text
    question_message = f'Вопрос {question_counter}:\n\n{message_text}\n\n#вопросы'
    try:
        await context.bot.send_message(chat_id=user_id, text=question_message)
        await update.message.reply_text('Ваш вопрос был отправлен администраторам.')
        question_counter += 1
    except Exception as e:
        await update.message.reply_text('Произошла ошибка при отправке сообщения.')

    await update.message.reply_text('Пишите сюда ваш следующий вопрос')

if __name__ == '__main__':
    application = Application.builder().token(bot_token).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text)

    application.add_handler(start_handler)
    application.add_handler(message_handler)

    application.run_polling()



