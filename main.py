import asyncio
import logging

from aiogram import Bot, Dispatcher, types

import config

logging.basicConfig(level=logging.INFO)

# Bot assignment--------------------------------------------------------------------------------------------------------
bot = Bot(token=config.TOKEN)
dp = Dispatcher()


@dp.message(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет, это эхо бот. Отправь любое сообщение и бот пришлет тебе такое же в ответ)"
    )


@dp.message()
async def with_puree(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
