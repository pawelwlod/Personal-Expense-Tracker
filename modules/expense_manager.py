# expense_manager.py
'''Expense Manager'''

from tabulate import tabulate
from dateutil import parser
from datetime import datetime
from modules import filter_manager
fm = filter_manager.FilterManager()

class ExpenseManager:
    '''Manages expenses for Personal Expense Tracker.'''
    def __init__(self, dm):
        '''Initialise ExpenseManager.'''
        self.dm = dm
        self.expenses = self.dm.load_data("expenses", {})
        self.categories = ['food', 'transport', 'entertainments', 'utilities', 'custom']
    
    def add_expense(self, amount, category, date):
        '''Adds an expense to the tracker.'''
        try:
            if amount:     
                if float(amount) > 0.00:
                    if category:
                        if category.lower() in self.categories:
                            if category.lower() == 'custom': category = str(input("Enter custom category: ")).title()
                            self.expenses[(len(self.expenses))] = {"date": date, "amount": float(amount), "category": category.title()}
                            self.dm.save_data("expenses", self.expenses)

                            print(f"\nAdded new expense for {date}: £{float(amount)} , {category.title()}")
                        else: print(f"Category {category} cant be selected.")
                    else: print("Expense category must be inputted!")
                else: print("Expense amount must be a positive number!")
            else: print("Expense amount must be inputted!")
        except parser.ParserError:
            print("Follow the format: YYYY-MM-DD !")
        except Exception as e:
            print(f"Error in add_expense: {str(e)}")
    
    def display_expenses(self):
        '''Displays all (with optional filters) expenses in a table-like form.'''
        try:
            filters = str(input("Select a filter (Category, Date, Amount, Multiple, skip for no filter): "))
            if filters.lower() == "category":
                filter_list = fm.filter_data(filters)
                if not filter_list: print("\nNo expenses matching the category.")
            
            elif filters.lower() == "date":
                start_date = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
                end_date = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d").date()
                if (start_date is None or end_date is None) or (start_date > end_date):
                    print("\nInvalid date range. Please try again."); return
                filter_list = fm.filter_date_range(start_date, end_date)
                if not filter_list: print("\nNo expenses in the date range.")
            
            elif filters.lower() == "amount":
                filter_list = fm.filter_data(filters)
                if not filter_list: print("\nNo expenses matching the amount.")
            
            elif filters.lower() == "multiple":
                mul_filters = []
                for _ in range(int(input("Enter filter amount (2 or 3): "))):
                    filter = str(input("Select a filter (Category, Date, Amount): ")).lower()
                    if filter in ["category", "date", "amount"]: mul_filters.append(filter)
                    else: print("\nUnavailable filter.")
                
                filter_list = fm.filter_multiple(mul_filters)
                if not filter_list: print("\nNo expenses matching given filters.")
            
            elif filters: return "\nInvalid filter."

            else: 
                filter_list = {}
                for key,value in self.expenses.items(): filter_list[key] = value

            total_spent, total_expenses = float(0), 0
            for _,b in filter_list.items():
                total_spent += b["amount"]; total_expenses += 1
            
            filter_list[len(filter_list)] = {"Total Amount Spent": total_spent, "Total Expenses": total_expenses}

            return tabulate(filter_list.values(), headers="keys", tablefmt="fancy_grid")
        except Exception as e:
            print(f"Error in display_expenses: {str(e)}")