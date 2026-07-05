from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "Ваш Токен."

async def start(update, context):
    await update.message.reply_text("Привет! Я бот. Напиши что-нибудь, я отвечу.")

async def handle_message(update, context):
    user_text = update.message.text
    await update.message.reply_text(f"Ты написал: {user_text}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен на PythonAnywhere...")
app.run_polling()