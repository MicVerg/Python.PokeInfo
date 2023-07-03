from fpdf import FPDF

user_input = input("Name: ")

# def set_text_color(self, 255, 255, 255):

class PDF(FPDF):
    def header(self):
        self.image("../shirtificate.png", 10, 8, 33)
        self.set_font("helvetica", "B", 16)
        self.cell(40, 10, user_input)


pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")