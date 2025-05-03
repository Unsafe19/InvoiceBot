class InvoicePDFGenerator:
    def generate(self, data):
        filename = f"invoice_{data['user']}.pdf"
        with open(filename, "w") as f:
            f.write(f"Invoice for {data['user']} with amount {data['amount']} UAH.")
        return filename