from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Бот запущен. Нажмите Ctrl+C для завершения")

def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Валютный бот")


def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		number = float(text)
		rate = 72.95
		rub = number * rate
		message = "$%.2f = %.2f руб" % (number, rub)
		context.bot.send_message(chat_id=chat.id, text=message)
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")

token = "1921095688:AAGBKHRe46VwyVs1xknEBXzYTZIGtH5xb0A"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()