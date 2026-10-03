# Expenses.py
'''Expenses Handler'''

from tabulate import tabulate
from dateutil import parser
from datetime import datetime

class ExpenseManager:
    '''Manages expenses for Personal Expense Tracker.'''
    def __init__(self, dm, fm, bm):
        '''Initialise ExpenseManager.'''
        self.dm         = dm
        self.fm         = fm
        self.bm         = bm
        self.expenses   = self.dm.load_data("expenses", {})
        self.categories = ['food', 'transport', 'entertainments', 'utilities', 'custom']
    
    def add_expense(self, amount: float, category: str, date: str):
        '''Adds an expense to the tracker.'''
        try:
            if not amount or not category or not date:
                return "Expense detaiks must be inputted!"
            if amount <= 0.00:
                return "Expense amount must be a positive number!"
            if category.lower() not in self.categories:
                return f"Category {category} cant be selected."
            if category.lower() == 'custom': 
                category = str(input("Enter custom category: ")).strip().title()
            
            self.expenses[(len(self.expenses))] = {
                "date":     date, 
                "amount":   amount, 
                "category": category
            }
            self.dm.save_data("expenses", self.expenses)
            
            if category in self.bm.budgets.keys():
                self.bm.spent_period(self.expenses)
                print(f"Added £{amount} to {category} spent amount.")
                print(f"£{self.bm.budgets[category]["remaining"]} remaining.")
            
            return f"\nAdded new expense for {date}: £{amount} , {category}"
        except parser.ParserError:
            return "Follow the format: YYYY-MM-DD !"
        except Exception as e:
            return f"Error in add_expense: {str(e)}"
    
    def display_expenses(self):
        '''Displays all (with optional filters) expenses in a table-like form.'''
        try:
            filters = str(input("Select a filter (Category, Date, Amount, Multiple, skip for no filter): ")).strip().lower()
            if filters in ['category', 'amount']:
                filter_list = self.fm.filter_data(filters, self.expenses)
                if not filter_list:
                    return "\nNo expenses matching the filter."
            
            elif filters == "date":
                start_date = datetime.strptime(input("Start date (YYYY-MM-DD): ").strip(), "%Y-%m-%d").date()
                end_date   = datetime.strptime(input("End date (YYYY-MM-DD): ").strip(), "%Y-%m-%d").date()
                if (start_date is None or end_date is None) or (start_date > end_date):
                    return "\nInvalid date range. Please try again."
                filter_list = self.fm.filter_date_range(start_date, end_date, self.expenses)
                if not filter_list: 
                    return "\nNo expenses in the date range."
            
            elif filters == "multiple":
                mul_filters = []
                for _ in range(int(input("Enter filter amount (2 or 3): ").strip())):
                    filter = str(input("Select a filter (Category, Date, Amount): ")).strip().lower()
                    if filter in ["category", "date", "amount"]: 
                        mul_filters.append(filter)
                    else: 
                        print("\nUnavailable filter.")
                
                filter_list = self.fm.filter_multiple(mul_filters=mul_filters, expenses=self.expenses)
                if not filter_list: 
                    return "\nNo expenses matching given filters."
            
            elif filters: 
                return "\nInvalid filter."

            else: 
                filter_list = {}
                for key, value in self.expenses.items(): 
                    filter_list[key] = value

            total_spent, total_expenses = float(0), 0
            for _, b in filter_list.items():
                total_spent    += b["amount"]
                total_expenses += 1
            
            filter_list[len(filter_list)] = {"Total Amount Spent": total_spent, "Total Expenses": total_expenses}

            return tabulate(filter_list.values(), headers="keys", tablefmt="fancy_grid")
        except Exception as e:
            print(f"Error in display_expenses: {str(e)}")