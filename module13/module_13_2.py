from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "TOKEN"

def start(update, context):
    print("Привет! Я бот помогающий твоему здоровью.")
    update.message.reply_text("Привет! Я бот помогающий твоему здоровью.")

def all_massages(update, context):
    print("Введите команду /start, чтобы начать общение.")
    update.message.reply_text("Введите команду /start, чтобы начать общение.")

updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.all, all_massages))

updater.start_polling()
updater.idle()
