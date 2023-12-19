from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time
from bs4 import BeautifulSoup
import requests as req

TOKEN = '5455438280:AAHZF7X7J7zt20zVEy2erEO3D69uFElkXfc'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(msg):
    result = time.localtime()
    if result.tm_min == 0:
        with open("index.html") as fp:
            resp = req.get("https://cbr.ru/")
            soup = BeautifulSoup(resp.text, 'lxml')