import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, month):
        self.amount = amount
        self.month = month

class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        to_pay = round(self.days_in_house/(self.days_in_house + flatmate2.days_in_house) * bill.amount, 2)
        #return f"{self.name} owes £{to_pay} this month ({bill.month})"
        return f"£{to_pay}"

class PDFreport:
    """
    Creates a PDF file that contains data about the flatmates such as their name, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF("P", "pt", "A4")
        pdf.add_page()

        #Add icon
        pdf.image("files\house.png", w=60, h=60)

        #Insert title
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

        pdf.output(self.filename)
        webbrowser.open(self.filename)



b = Bill(120, "Jan 2021")
f1 = Flatmate("Rob", 17)
f2 = Flatmate("Jon", 9)

f1.pays(b, f2)

pdf_report = PDFreport("Report1.pdf")
pdf_report.generate(f1, f2, b)