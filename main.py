import logging
import asyncio
from aiogram import Bot, Dispatcher
import key
from body import common, kamera


async def main():
    API_TOKEN = key.token

    # Включаем логирование, чтобы видеть сообщения в консоли
    logging.basicConfig(level=logging.INFO)

    # Инициализация бота и диспетчера
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.include_router(kamera.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
