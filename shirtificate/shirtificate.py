from fpdf import FPDF



# def set_text_color(self, 255, 255, 255):

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32)
        self.cell(0, 0, "CS50 Shirtificate", border=0, align="C")


    def body():
        self.image("./shirtificate.png", x = 30, y = 50, w = 150, h = 150)
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255, 255, 255)


def main():
    user_input = input("Name: ")
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    shirt_text = f"{user_input} took CS50"
    pdf.body(shirt_text)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()