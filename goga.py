import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import requests
import json

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токены
BOT_TOKEN = '7381587751:AAFId-MmspFToMOxlV87_OEqS98C7ddgAKE'
OPENROUTER_API_KEY = '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'
gemini_api = 'AIzaSyCtgCMK6wovz5H7WOeEsiV-LCVoP1tEnQM'
from openai import OpenAI

DEEPSEEK_API = 'sk-b6f582bec1bf400da48b132a659679d8'


# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

from google.genai import types as google_types

from google import genai

client = genai.Client(api_key=gemini_api)


@dp.message(CommandStart())
async def start_command(message: Message):
    print('huy')
    await message.answer("Привет! Я крутой бизнес-инфо-цыга, задавай свои ответы, иначе я тебя отпинаю.")

# Обработка текстовых сообщений
@dp.message()
async def handle_message(message: Message):
    user_input = message.text

    # Формирование запроса к OpenRouter API
    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input,
            config=google_types.GenerateContentConfig(
                system_instruction="Ты профессиональный бизнес коуч Алексей. У тебя умер сын от рака толстой кишки, Ещё ты гей и немного груб"

        ))

        print(response.text)


        await message.answer(response.text)

    except Exception as e:
        logging.error(f"Ошибка при запросе к OpenRouter: {e}")
        await message.answer("Извините, произошла ошибка. Попробуйте позже.")


async def main():
    await dp.start_polling(bot)
# В конце файла измените запуск бота:
if __name__ == "__main__":
    asyncio.run(main())