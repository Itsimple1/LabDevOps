import asyncio
import logging
from aiogram import Bot, Dispatcher, types

import sys

logging.basicConfig(level=logging.INFO)

# Bot assignment--------------------------------------------------------------------------------------------------------
bot = Bot(sys.argv[1])
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Бот готов работать. Для запроса введите любую цифру")


@dp.message_handler()
async def with_puree(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
