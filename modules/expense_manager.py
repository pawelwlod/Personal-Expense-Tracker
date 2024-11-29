# expense_manager.py
'''Expense Manager'''

from tabulate import tabulate
from data_manager import DataManager
dm = DataManager()

class ExpenseManager:
    '''Personal Expense Tracker functions.'''
    def __init__(self):
        '''Initialise ExpenseManager.'''
        self.expenses = dm.load_data({})
    
    def add_expense(self, amount, category, date):
        '''Adds an expense to the tracker.'''
        categories = ['Food', 'Transport', 'Games', 'Other']

        if len(date) == 10:
            if float(amount) > 0.00:
                if category in categories:
                    self.expenses[date] = {"amount": amount, "category": category}
                    dm.save_data(self.expenses)

                    print(f"\nAdded new expense for {date}: £{amount} , {category}")
                else:
                    print(f"Category {category} cant be selected.")
            else:
                print(f"Expense amount must be a positive number!")
        else:
            print("Follow the date format: YYYY-MM-DD")
    
    def display_expenses(self):
        '''Displays all expenses in a table-like form.'''
        print(tabulate(self.expenses.items(), headers=['Date', 'Amount/Category', 'Category'], tablefmt="fancy_grid"))