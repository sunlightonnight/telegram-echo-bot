from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests

TOKEN = "8301890883:AAEk-MqoEfml5nE38Onk9rPjVb7XxxvJfHk"

async def start(update, context):
    await update.message.reply_text("Привет! Я бот. Напиши что-нибудь, я отвечу.")

async def handle_message(update, context):
    user_text = update.message.text
    await update.message.reply_text(f"Ты написал: {user_text}")

async def currency(update, context):
    await update.message.reply_text("Напиши валюту которую хочешь перевести в рубли в формате: /currency USD 100")
    if len(context.args) < 2:
        await update.message.reply_text("Напиши в формате: /currency USD 100")
        return

    valute = context.args[0].upper()
    try:
        amount = float(context.args[1])
    except ValueError:
        await update.message.reply_text("Сумма должна быть числом.")
        return

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]

    if valute not in rates:
        await update.message.reply_text("Такой валюты нет. Используй: USD, EUR, KZT и т.д.")
        return

    result = amount * rates["RUB"] / rates[valute]

    await update.message.reply_text(f"{amount} {valute} = {result:.2f} RUB")
        
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("currency", currency))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен....")
app.run_polling()