from datetime import datetime
from openpyxl import load_workbook


def validate(date_text):
    try:
        datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False


class Transaction:
    def __init__(self, month_year, date, name, amount, account):
        self.month_year = month_year
        self.date = date
        self.name = name
        self.amount = amount
        self.account = account

    def __str__(self) -> str:
        return """my: [%s], date: [%s], desc: [%s], amount: [%.2f], account: [%s]""" % \
               (self.month_year,  self.date, self.name, self.amount, self.account)


def read_isracard(file):
    month = '_'.join(file.split('/')[-1].split('_')[1:3])
    workbook = load_workbook(filename=file)
    sheet = workbook["Transactions"]
    legal_transaction = []
    account = ''
    abroad = False

    for row in sheet.iter_rows():
        if row[0].value is not None:
            if row[1].value == 'מועד חיוב':
                account = row[0].value.replace('*', '').split('-')[-1].strip()
                abroad = False
            elif row[0].value == 'עסקאות בחו˝ל':
                abroad = True
            elif validate(row[0].value) is True:
                if abroad:
                    legal_transaction.append(Transaction(month, row[0].value, row[2].value, row[5].value, account))
                else:
                    legal_transaction.append(Transaction(month, row[0].value, row[1].value, row[4].value, account))
    return legal_transaction

