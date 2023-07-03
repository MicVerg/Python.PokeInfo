from fpdf import FPDF

user_input = input("Name: ")

# def set_text_color(self, 255, 255, 255):

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png").Align("C)
        self.set_font("helvetica", "B", 16)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        self.cell(-80)
        self.cell(40, 10, user_input)


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.output("shirtificate.pdf")