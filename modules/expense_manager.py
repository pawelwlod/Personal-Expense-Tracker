# expense_manager.py
'''Expense Manager'''

from data_manager import DataManager
dm = DataManager()

class ExpenseManager:
    '''Personal Expense Tracker functions.'''
    def __init__(self):
        '''Initialise ExpenseManager.'''
        self.expenses = {}
    
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