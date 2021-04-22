from flat import Bill, Flatmate
from reports import PDFReport

amount = float(input("Hi user, enter the bill amount: £"))
period = input("What is the bill period (e.g. Dec 2020): ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the other flatmate's name? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

bill = Bill(amount, period)
f1 = Flatmate(name1, days_in_house1)
f2 = Flatmate(name2, days_in_house2)

pdf_report = PDFReport(f"{bill.month}.pdf")
pdf_report.generate(f1, f2, bill)
