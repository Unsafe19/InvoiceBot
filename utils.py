from constants import DEFAULT_AMOUNT

def extract_invoice_data(update):
    return {
        "user": update.effective_user.first_name,
        "amount": DEFAULT_AMOUNT
    }

def save_invoice_record(data, pdf_path):
    print(f"Збережено рахунок для {data['user']} у файлі {pdf_path}")

def send_invoice(update, context, pdf_path):
    update.message.reply_text(f"Ваш рахунок створено: {pdf_path}")

def build_user_message(user_name):
    return f"Привіт, {user_name}! Чим можу допомогти?"