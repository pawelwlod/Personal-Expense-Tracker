# Budgets.py
'''Budgets Handler'''

import time
from tabulate import tabulate
from datetime import datetime, timedelta
import utils

class BudgetManager:
    '''Manages budgets for Personal Expense Tracker'''
    def __init__(self, dm, fm):
        '''Initialise BudgetManager.'''
        self.dm                 = dm
        self.fm                 = fm
        self.utils              = utils.Utils(self)
        self.budgets            = self.dm.load_data("budgets", {})
        self.default_categories = ['food', 'transport', 'entertainments', 'utilities']
        
        for category in self.default_categories:
            if category.title() not in self.budgets.keys():
                self.utils.header()
                print(f"\n{category.title()} is a default budget, please give it a limit and period.")
                budget_limit  = float(input("Enter budget limit: ").strip())
                budget_period = str(input("Enter budget period: (Weekly, Monthly, Yearly) ")).strip().title()
                
                self.add_budget(category, budget_limit, budget_period); 
                time.sleep(3)

    def add_budget(self, name: str, limit: float, period: str):
        '''Adds new budget to Personal Expense Tracker.'''
        try:
            if not name or not limit or not period:
                return "Budget name, limit, and period need to be inputted!"            
            if name.title() in self.budgets.keys():
                return f"{name.title()} is already has a set budget."            
            if limit <= 0:
                return "Budget limit needs to be more than 0."
            
            self.budgets[name.title()] = {
                "name":      name, 
                "limit":     limit, 
                "period":    period, 
                "spent":     0, 
                "remaining": limit,
                "options":   None
            }
            self.dm.save_data("budgets", self.budgets)
    
            return f"\nAdded new budget for {name.title()}: £{float(limit)}, {period.title()}"
        except Exception as e:
            return f"Error in add_budget: {str(e)}"

    def edit_budget(self, choice: str, name: str, value: str):
        '''Edits existing budget in Personal Expense Tracker.'''
        try:
            if not choice or not name or not value:
                return "Budget name and edit choice must be inputted!"
            if name.title() not in self.budgets.keys():
                return f"{name.title()} doesn't have a set budget."
            
            print(f"\n{name.title()} : £{self.budgets[name.title()]["limit"]}, {self.budgets[name.title()]['period']}")
            if choice.lower() in ['limit', 'period']:
                self.budgets[name.title()][choice.lower()] = float(value) if choice.lower() == 'limit' else str(value.title())
                self.dm.save_data("budgets", self.budgets)
                
                return f"Budget {choice.lower()} for {name.title()} edited to: {f"£{value}" if choice.lower() == 'limit' else value.title()}"

            return "Edit choice not limit or period!"
        except Exception as e:
            return f"Error in edit_budget: {str(e)}"

    def display_budgets(self):
        '''Displays all or filtered budgets.'''
        try:
            name = str(input("Enter budget to display (empty to show all): ")).strip().title()
            if not name:
                return tabulate(self.budgets.values(), headers="keys", tablefmt="fancy_grid")
            if name in self.budgets.keys():
                return tabulate([self.budgets[name]], headers="keys", tablefmt="fancy_grid")
            
            return f"{name} not found in budgets."
        except Exception as e:
            print(f"Error in display_budgets: {str(e)}")

    def delete_budget(self, name: str):
        '''Deletes existing budget from Personal Expense Tracker.'''
        try:
            if not name:
                return "Budget name must be inputted!"
            if name.title() not in self.budgets.keys():
                print(f"{name.title()} not found in budgets.")
            confirmation = str(input(f"\nAre you sure you want to delete your budget for {name.title()}? (Y/N) ")).strip().lower()
            if confirmation == "y":
                del self.budgets[name.title()]
                self.dm.save_data("budgets", self.budgets)
            
                return f"Budget for {name.title()} has been deleted."
            else: 
                return "Deletion cancelled."
        except Exception as e:
            return f"Error in delete_budget: {str(e)}"

    def spent_period(self, expenses: dict):
        '''Calculates expense amount for each budget during its period.'''
        try:
            today = datetime.today().date()
            for name, budget in self.budgets.items():
                filtered_expenses = {}
                if budget["period"].lower() == "weekly":
                    start_date        = today - timedelta(days=today.weekday())
                    end_date          = start_date + timedelta(days=6)
                    filtered_expenses = self.fm.filter_date_range(start_date, end_date, expenses)

                elif budget["period"].lower() == "monthly":
                    start_date        = datetime(today.year, today.month, 1).date()
                    end_month         = datetime(today.year, today.month + 1, 1).date() if today.month != 12 else datetime(today.year + 1, 1, 1).date()
                    end_date          = end_month - timedelta(days=1)
                    filtered_expenses = self.fm.filter_date_range(start_date, end_date, expenses)
                
                elif budget["period"].lower() == "yearly":
                    start_date        = datetime(today.year, 1, 1).date()
                    end_date          = datetime(today.year + 1, 1, 1).date()
                    filtered_expenses = self.fm.filter_date_range(start_date, end_date, expenses)

                if filtered_expenses:
                    amount = 0
                    for expense in filtered_expenses.values():
                        if name.title() == expense["category"]:
                            amount += expense["amount"]

                    if (budget["limit"] - amount) <= 0:
                        self.budgets[name.title()]["options"] = "alert"
                    elif (budget["limit"] - amount) <= 10:
                        self.budgets[name.title()]["options"] = "warn"
                    else:
                        self.budgets[name.title()]["options"] = None

                    self.budgets[name.title()]["spent"]     = amount
                    self.budgets[name.title()]["remaining"] = budget["limit"] - amount
                    self.dm.save_data("budgets", self.budgets)
                else:
                    self.budgets[name.title()]["spent"]     = 0
                    self.budgets[name.title()]["remaining"] = budget["limit"]
                    self.budgets[name.title()]["options"]   = None
                    self.dm.save_data("budgets", self.budgets)
        except Exception as e:
            print(f"Error in spent_period: {str(e)}")