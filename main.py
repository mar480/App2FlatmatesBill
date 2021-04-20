class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, month):
        self.amount = amount
        self.month = month
        self.period = self.get_period(month)

    def get_period(self, month):
        period = {
            "Jan" : 31,
            "Feb": 28,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August": 31,
            "Sept": 30,
            "Oct": 31,
            "Nov": 30,
            "Dec": 31,
        }
        return period.get(month)


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return round((self.days_in_house/bill.period) * bill.amount, 2)

class PDFreport:
    """
    Creates a PDF file that contains data about the flatmates such as their name, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass