import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = ""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Добро пожаловать!\n")

@router.message()
async def fallback_command(message: Message):
    await message.reply("Неизвестная команда. Используйте /start, чтобы увидеть доступные команды.")

async def main() -> None:
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
