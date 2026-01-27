# budget_manager.py
'''Budget Manager'''

import time
from tabulate import tabulate
from datetime import datetime, timedelta

class BudgetManager:
    '''Manages budgets for Personal Expense Tracker'''
    def __init__(self, dm, fm, utils):
        '''Initialise BudgetManager.'''
        self.dm                 = dm
        self.fm                 = fm
        self.utils              = utils
        self.budgets            = self.dm.load_data("budgets", {})
        self.default_categories = ['food', 'transport', 'entertainments', 'utilities']
        
        for category in self.default_categories:
            if category.title() not in self.budgets.keys():
                self.utils.header()
                print(f"\n{category.title()} is a default budget, please give it a limit and period.")
                budget_limit  = str(input("Enter budget limit: "))
                budget_period = str(input("Enter budget period: (Weekly, Monthly, Yearly) "))
                
                self.add_budget(category, budget_limit, budget_period); 
                time.sleep(3)

    def add_budget(self, name, limit, period):
        '''Adds new budget to Personal Expense Tracker.'''
        try:
            if name and limit and period:
                if name.title() not in self.budgets.keys():
                    if float(limit) > 0:
                        self.budgets[name.title()] = {
                            "name":      name.title(), 
                            "limit":     float(limit), 
                            "period":    period.title(), 
                            "spent":     0, 
                            "remaining": float(limit),
                            "options":   None
                        }
                        self.dm.save_data("budgets", self.budgets)

                        print(f"\nAdded new budget for {name.title()}: £{float(limit)}, {period.title()}")
                    else: 
                        print("Budget limit needs to be more than 0.")
                else: 
                    print(f"{name.title()} is already has a set budget.")
            else: 
                print("Budget name, limit, and period need to be inputted!")
        except Exception as e:
            print(f"Error in add_budget: {str(e)}")

    def edit_budget(self, choice, name, value):
        '''Edits existing budget in Personal Expense Tracker.'''
        try:
            if choice and name and value:
                if name.title() in self.budgets.keys():
                    print(f"\n{name.title()} : £{self.budgets[name.title()]["limit"]}, {self.budgets[name.title()]['period']}")
                    
                    if choice.lower() == 'amount':
                        self.budgets[name.title()]["limit"] = float(value)
                        print(f"Budget amount for {name.title()} edited to: £{value}")
                    elif choice.lower() == 'period':
                        self.budgets[name.title()]["period"] = str(value.title())
                        print(f"Budget period for {name.title()} edited to: {value.title()}")
                    
                    self.dm.save_data("budgets", self.budgets)
                else: 
                    print(f"{name.title()} doesn't have a set budget.")
            else: 
                print("Budget name must be inputted!")
        except Exception as e:
            print(f"Error in edit_budget: {str(e)}")

    def display_budgets(self):
        '''Displays all or filtered budgets.'''
        try:
            name = str(input("Enter budget to display (empty to show all): "))
            list = {}
            if name:
                for key,values in self.budgets.items():
                    if name.title() == key:
                        list[name.title()] = values
                        return tabulate(list.values(), headers="keys", tablefmt="fancy_grid")
                else: 
                    return f"{name.title()} not found in budgets."
            else: 
                return tabulate(self.budgets.values(), headers="keys", tablefmt="fancy_grid")
        except Exception as e:
            print(f"Error in display_budgets: {str(e)}")

    def delete_budget(self, name):
        '''Deletes existing budget from Personal Expense Tracker.'''
        try:
            if name:
                if name.title() in self.budgets.keys():
                    confirmation = str(input(f"\nAre you sure you want to delete your budget for {name.title()}? (Y/N) "))
                    if confirmation.lower() == "y":
                        del self.budgets[name.title()]
                        self.dm.save_data("budgets", self.budgets)

                        print(f"Budget for {name.title()} has been deleted.")
                    else: 
                        print("Deletion cancelled.")
                else: 
                    print(f"{name.title()} not found in budgets.")
            else: 
                print("Budget name must be inputted!")
        except Exception as e:
            print(f"Error in delete_budget: {str(e)}")

    def spent_period(self, expenses):
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