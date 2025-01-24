# expense_manager.py
'''Expense Manager'''

from tabulate import tabulate
from dateutil import parser
from modules import data_manager
dm = data_manager.DataManager()
dtm = data_manager.DateManager()

class ExpenseManager:
    '''Personal Expense Tracker functions.'''
    def __init__(self):
        '''Initialise ExpenseManager.'''
        self.expenses = dm.load_data({})
        self.categories = ['food', 'transport', 'entertainments', 'utilities', 'custom']
    
    def add_expense(self, amount, category, date):
        '''Adds an expense to the tracker.'''
        try:
            if amount:     
                if float(amount) > 0.00:
                    if category:
                        if category.lower() in self.categories:
                            if category.lower() == 'custom':
                                category = str(input("Enter custom category: ")).title()
                            self.expenses[(len(self.expenses))] = {"date": date, "amount": float(amount), "category": category.title()}
                            dm.save_data(self.expenses)

                            print(f"\nAdded new expense for {date}: £{float(amount)} , {category.title()}")
                        else:
                            print(f"Category {category} cant be selected.")
                    else:
                        print("Expense category must be inputted!")
                else:
                    print("Expense amount must be a positive number!")
            else:
                print("Expense amount must be inputted!")
        except parser.ParserError:
            print("Follow the format: YYYY-MM-DD !")
        except Exception as e:
            print(f"Error in add_expense: {str(e)}")
    
    def display_expenses(self):
        '''Displays all (with optional filters) expenses in a table-like form.'''
        try:
            filters = str(input("Select a filter (Category, Date, skip for no filter): "))
            if filters.lower() == "category":
                filter_category = str(input(f"Filter by category: ({' '.join(str(e.title()) for e in self.categories)}) "))
                filter_list = dm.filter_category(self.expenses, filter_category)
                if not filter_list:
                    print("\nNo expenses matching the category.")
            
            elif filters.lower() == "date":
                start_date, end_date = dtm.validate_date_range(input("Start date (YYYY-MM-DD): "), input("End date (YYYY-MM-DD): "))
                if start_date is None or end_date is None:
                    print("\nInvalid date range. Please try again.")
                    return
                filter_list = dtm.filter_date_range(self.expenses, start_date, end_date)
                if not filter_list:
                    print("\nNo expenses in the date range.")
            
            else:
                 filter_list = self.expenses

            return tabulate(filter_list.values(), headers="keys", tablefmt="fancy_grid")
        except Exception as e:
            print(f"Error in display_expenses: {str(e)}")