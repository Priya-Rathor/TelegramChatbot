from dotenv import load_dotenv
import os
from aiogram import Bot,Dispatcher,executor,types
import openai
import sys

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KAY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    '''
    A class to store previously  response fro the chatAPI
    '''
    def __init__(self) ->None:
        self.refernce = ""


reference = Reference()
model_name = "gpt-3.5-turbo"

bot =Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def welcome(message:types.Message):
    """
    This handler receives messages with '/start' or '/help' command
    """

    await message.reply("Hi\n I am Tele Bot!\ Created by me. How can i assist you ")


@dispatcher.message_handler(commands=['help'])
async def helper(message:types.Message)
    """
    A handler to display the help menu.
    """
    help_command = """
     
    Hi There ,I'm Telegram bot create by  me ! please follow these commands
    /start - to start the conversation\
    /clear - to clear the past conversation and  context.
    /help - to get this help menu.
    I hope this helps. :)
    """

    await message.reply(help_command)




if __name__ == "__main__":
  executor.start_polling(dispatcher,skip_updates = True  )