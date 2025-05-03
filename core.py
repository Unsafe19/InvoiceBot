from utils import extract_invoice_data, save_invoice_record, send_invoice

def create_invoice(update, context, pdf_generator):
    data = extract_invoice_data(update)
    pdf_path = pdf_generator.generate(data)
    save_invoice_record(data, pdf_path)
    send_invoice(update, context, pdf_path)