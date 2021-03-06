import webbrowser
import os
from fpdf import FPDF


class PDFReport:
    """
    Creates a PDF file with data about the flatmates such as their name, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF("P", "pt", "A4")
        pdf.add_page()

        # Add icon
        pdf.image(r"files\house.png", w=60, h=60)

        # Insert title
        pdf.set_font(family="Arial", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        # Insert period
        pdf.set_font(family="Times", size=18, style="B")
        pdf.cell(w=100, h=40, txt="Period:")
        pdf.cell(w=150, h=40, txt=bill.month, ln=1)

        # Insert name and due amount of flatmate1
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill, flatmate2)), ln=1)

        # Insert name and due amount of flatmate2
        pdf.cell(w=100, h=25, txt=flatmate2.name)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill, flatmate1)), ln=1)

        #change directory to files and output and open the pdf
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)