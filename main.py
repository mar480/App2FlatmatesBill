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
        return f"{self.name} owes £{to_pay} this month ({bill.month})"

class PDFreport:
    """
    Creates a PDF file that contains data about the flatmates such as their name, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass