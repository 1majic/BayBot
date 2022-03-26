from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# import main

API_TOKEN = "1919329712:AAFpnJdE9FWJTscASFXyJr3HekrOv49TNj4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, я виртуальный интелект созданный ради развлечения... Ха-ха😅...\nЗадавай свой вопрос')


@dp.message_handler()
async def getIntent(message: types.Message):
    await message.answer(main.get_intent_by_model(message.text))


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
