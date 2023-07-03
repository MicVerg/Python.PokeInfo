from fpdf import FPDF

user_input = input("Name: ")

# def set_text_color(self, 255, 255, 255):

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", x = 30, y = 50, w = 150, h = 150)
        self.set_font("helvetica", "B", 32)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        self.cell(-80)
        self.cell(700, 300, user_input)


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.output("shirtificate.pdf")

