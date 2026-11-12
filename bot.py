import os
import anthropic
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": update.message.text}],
    )
    await update.message.reply_text(msg.content[0].text)

app = ApplicationBuilder().token(os.environ["TELEGRAM_TOKEN"]).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_polling()
