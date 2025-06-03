import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datebase

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я ваш новый бот.")

# Основная функция для запуска бота
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable is not set")
    updater = Updater(token)
    dp = updater.dispatcher

    # Обработчик для команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
