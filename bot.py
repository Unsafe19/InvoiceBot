from core import create_invoice
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Вітаю! Використайте /invoice для створення рахунку.")

def invoice(update, context):
    from pdf_generator import InvoicePDFGenerator
    pdf_gen = InvoicePDFGenerator()
    create_invoice(update, context, pdf_gen)

updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("invoice", invoice))

updater.start_polling()
updater.idle()