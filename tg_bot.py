import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Application
from telegram.ext import ContextTypes
from telegram.ext import ChatJoinRequestHandler
import requests

TOKEN="5815046882:AAEda4DeKsDr3N2TadHINxuqW_De1CwYONc"
BOT_username='@Sar_vivi_bot'

async def send_messeng(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params={
        'chat_id': chat_id,
        'text': "HELLO ITS ME MARIOO BOOT XUIII"
    }
    response = requests.post(url, params)
    await requests.post(url, params)
    if response.status_code == 200:
        print('Повідомлення успішно надіслано!')
    else:
        print('Помилка при надсиланні повідомлення.')

async def join_request(update, context):
    await context.bot.approve_chat_join_request(
            chat_id=update.effective_chat.id, user_id=update.effective_user.id
        )
    print(update.effective_user.id,"\n", update.effective_user.first_name, "\n", update.effective_user.last_name,"\n", update.effective_user.username )
    send_messeng(update.effective_user.id)

async def update_bace():
    pass
async def start_comand(update:Updater,context:ContextTypes.DEFAULT_TYPE):
    print('HI!')
    await update.message.reply_text('Привіт, що робиш?')

async def help_comand(update:Updater,context:ContextTypes.DEFAULT_TYPE):
    print('HEELP')
    await update.message.reply_text('Чим можу допомгти?')

async def custom_comand(update:Updater,context:ContextTypes.DEFAULT_TYPE):
    print('CustomSEXS')
    await update.message.reply_text('Ого ніхуя собі')

def handler(text):
    pass


if __name__=='__main__':
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_comand))
    app.add_handler(CommandHandler('help',help_comand))
    app.add_handler(CommandHandler('custom',custom_comand))
    app.add_handler(ChatJoinRequestHandler(join_request))
    print('YES')
    app.run_polling(poll_interval=3)
