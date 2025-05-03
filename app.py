from flask import Flask, render_template, request, send_file
from generate_pdf import create_invoice_pdf
from email_sender import send_email
import sqlite3
import os
import logging
import unicodedata

app = Flask(__name__)

if not os.path.exists('invoices'):
    os.makedirs('invoices')

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def normalize_filename(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

@app.route('/', methods=['GET', 'POST'])
def invoice_form():
    if request.method == 'POST':
        client_name = request.form['client_name']
        service = request.form['service']
        amount = request.form['amount']
        email = request.form['email']

        safe_client_name = normalize_filename(client_name.replace(' ', '_'))
        filename = f"invoices/{safe_client_name}_invoice.pdf"
        create_invoice_pdf(client_name, service, amount, filename)

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS invoices (client TEXT, service TEXT, amount REAL, email TEXT)')
        c.execute('INSERT INTO invoices (client, service, amount, email) VALUES (?, ?, ?, ?)',
                  (client_name, service, amount, email))
        conn.commit()
        conn.close()

        logging.info(f"Створено рахунок для {client_name} на суму {amount} грн")

        try:
            send_email(
                receiver_email=email,
                subject="Ваш рахунок",
                body=f"Доброго дня, {client_name}!\nУ додатку ваш рахунок за послугу {service} на суму {amount} грн.",
                attachment_path=filename,
                sender_email="ТВОЯ_ПОШТА@gmail.com",
                sender_password="ТВОЙ_ПАРОЛЬ_ДОДАТКУ"
            )
            logging.info(f"Email відправлено на {email}")
        except Exception as e:
            logging.error(f"Помилка відправки email: {str(e)}")

        return send_file(filename, as_attachment=True)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
