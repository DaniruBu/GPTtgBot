import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types, executor
import openai

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

openai.api_key = (os.getenv('OPENAI_API_KEY'))


@dp.message_handler()
async def echo(message: types.Message):
    # Генерация ответа
    response = openai.Completion.create(
        model="text-davinci-003", # Используйте свою модель
        prompt=message.text,
        max_tokens=150,
        temperature=0.2
    )

    # Отправка ответа
    await message.answer(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)