from fpdf import FPDF

user_input = input("Name: ")

def set_text_color(self, 255, 255, 255)

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, user_input)
pdf.output("shirtificate.pdf")