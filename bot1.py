from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datebase

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я ваш новый бот.")

# Основная функция для запуска бота
def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    updater = Updater("7267717438:AAEc_ENZqkM8wfvzLIBh1bEo1UGBEz1qzmk")
    dp = updater.dispatcher

    # Обработчик для команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()