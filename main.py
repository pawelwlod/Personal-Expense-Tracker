# main.py

import sys
sys.path.insert(0, 'modules')
from expense_manager import ExpenseManager

expense_manager = ExpenseManager()

date = str(input("Enter date (YYYY-MM-DD): "))
amount = float(input("Enter expense amount (format: £0.00): "))
category = str(input("Enter category (Food, Transport, Games, Other): "))

expense_manager.add_expense(amount=amount, category=category, date=date)