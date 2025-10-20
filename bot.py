import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 🔹 ВСТАВЬ СВОЙ ТОКЕН от @BotFather
TOKEN = "8395434139:AAFuS-gsmSVjcxdHbEqRHEltq4Xn8992Dkw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Я твой первый Telegram-бот.\n\n"
        "Напиши /help, чтобы узнать, что я умею."
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📚 Команды, которые я понимаю:\n"
        "/start — запустить бота\n"
        "/help — помощь\n\n"
        "Скоро здесь появятся новые функции 🚀"
    )

async def main():
    print("Бот запущен ✅")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    

