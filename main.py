from telegram import Update
from telegram.ext import Application, CommandHandler
from analyzer import get_gold_price, analyze_price
import os

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TOKEN")

# شروع بات
async def start(update: Update
