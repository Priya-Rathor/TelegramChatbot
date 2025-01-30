from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")  # Fixed typo
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    """Stores previous chat responses"""
    def __init__(self):
        self.reference = ""  # Fixed typo

reference = Reference()
model_name = "gpt-3.5-turbo"

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """Clears past conversation history"""
    reference.reference = ""

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hi! I am Tele Bot! Created by me. How can I assist you?")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
    Hi There, I'm a Telegram bot! Here are my commands:
    /start - Start the conversation
    /clear - Clear the past conversation and context
    /help - Show this help menu
    """
    await message.reply(help_command)

chat_history = []

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    global chat_history

    chat_history.append({"role": "user", "content": message.text})
    
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=chat_history
    )
    
    bot_response = response['choices'][0]['message']['content']
    chat_history.append({"role": "assistant", "content": bot_response})

    await bot.send_message(chat_id=message.chat.id, text=bot_response)

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)
