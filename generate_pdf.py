from fpdf import FPDF

def create_invoice_pdf(client_name, service, amount, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)  # Додамо кириличний шрифт
    pdf.set_font('DejaVu', '', 12)

    pdf.cell(200, 10, txt="Рахунок-фактура", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Клієнт: {client_name}", ln=True)
    pdf.cell(200, 10, txt=f"Послуга: {service}", ln=True)
    pdf.cell(200, 10, txt=f"Сума: {amount} грн", ln=True)

    pdf.output(filename)
