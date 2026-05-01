import asyncio
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load .env file
load_dotenv()

# Get token from .env
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! 👋\nUse this command:\n/remind <minutes> <message>\n\nExample:\n/remind 1 Drink water"
    )

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        minutes = int(context.args[0])
        message = " ".join(context.args[1:])

        await update.message.reply_text(f"✅ Reminder set for {minutes} minutes")

        await asyncio.sleep(minutes * 60)

        await update.message.reply_text(f"⏰ Reminder: {message}")

    except:
        await update.message.reply_text("❌ Usage: /remind 1 Test")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("remind", remind))

app.run_polling()