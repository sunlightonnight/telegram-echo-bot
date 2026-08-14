# Telegram-бот-помощник

Простой Telegram-бот на Python. Отвечает на сообщения и умеет конвертировать валюты.

A simple Telegram bot in Python. Replies to messages and can convert currencies.

---

## Как запустить / How to run

1. Установи Python 3.x
2. Установи библиотеки: `pip install requests python-telegram-bot`
3. Скачай файл `tgbot1.py`
4. Замени `8301890883:AAEk-MqoEfml5nE38Onk9rPjVb7XxxvJfHk` на свой токен от @BotFather
5. Запусти: `python tgbot1.py`

1. Install Python 3.x
2. Install libraries: `pip install requests python-telegram-bot`
3. Download `tgbot1.py`
4. Replace `8301890883:AAEk-MqoEfml5nE38Onk9rPjVb7XxxvJfHk` with your token from @BotFather
5. Run: `python tgbot1.py`

---

## Команды / Commands

- `/start` — приветствие / greeting
- `/currency USD 100` — конвертирует 100 долларов в рубли / converts 100 USD to RUB

---

## Пример / Example

**Пользователь:** Привет!
**Бот:** Ты написал: Привет!

**Пользователь:** /currency USD 100
**Бот:** 100.0 USD = 8500.00 RUB

---

## Код / Code

```python
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests

TOKEN = "8301890883:AAEk-MqoEfml5nE38Onk9rPjVb7XxxvJfHk"

async def start(update, context):
    await update.message.reply_text("Привет! Я бот. Напиши что-нибудь, я отвечу.")

async def handle_message(update, context):
    user_text = update.message.text
    await update.message.reply_text(f"Ты написал: {user_text}")

async def currency(update, context):
    if len(context.args) < 2:
        await update.message.reply_text("Напиши: /currency USD 100")
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
```
---

## Автор / Author

**sunlightonnight**

---

## Лицензия / Licence

MIT
