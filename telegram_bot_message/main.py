import telebot

TOKEN = 'BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)


def message_user(request):
    telegram_chat = 'TELEGRAM_CHAT_ID'
    bot.send_message(telegram_chat, 'Hello, World!')
    return
