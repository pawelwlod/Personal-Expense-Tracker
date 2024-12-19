# expense_manager.py
'''Expense Manager'''

from tabulate import tabulate
from dateutil import parser
from modules import data_manager
dm = data_manager.DataManager()

class ExpenseManager:
    '''Personal Expense Tracker functions.'''
    def __init__(self):
        '''Initialise ExpenseManager.'''
        self.expenses = dm.load_data({})
    
    def add_expense(self, amount, category, date):
        '''Adds an expense to the tracker.'''
        categories = ['food', 'transport', 'games', 'other']

        try:
            if parser.parse(date):
                if amount:     
                    if float(amount) > 0.00:
                        if category:
                            if category.lower() in categories:
                                self.expenses[(len(self.expenses))] = {"date": date, "amount": float(amount), "category": category}
                                dm.save_data(self.expenses)

                                print(f"\nAdded new expense for {date}: £{float(amount)} , {category}")
                            else:
                                print(f"Category {category} cant be selected.")
                        else:
                            print("Expense category must be inputted!")
                    else:
                        print("Expense amount must be a positive number!")
                else:
                    print("Expense amount must be inputted!")
            else:
                print("Follow the date format: YYYY-MM-DD")
        except parser.ParserError:
            print("Follow the format: YYYY-MM-DD !")
        except Exception as e:
            print(f"Error in add_expense: {str(e)}")
    
    def display_expenses(self):
        '''Displays all expenses in a table-like form.'''
        try:
            return tabulate(self.expenses.values(), headers="keys", tablefmt="fancy_grid")
        except Exception as e:
            print(f"Error in display_expenses: {str(e)}")