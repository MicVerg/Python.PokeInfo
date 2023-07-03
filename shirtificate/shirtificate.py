from fpdf import FPDF

user_input = input("Name: ")

# def set_text_color(self, 255, 255, 255):

class PDF(FPDF):
    def header(self):
        self.image("../shirtificate.png", 10, 8, 33)
        self.set_font("helvetica", "B", 16)
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.cell(40, 10, user_input)
pdf.output("shirtificate.pdf")