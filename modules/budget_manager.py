# budget_manager.py
'''Budget Manager'''

from tabulate import tabulate

class BudgetManager:
    '''Manages budgets for Personal Expense Tracker'''
    def __init__(self, dm, em):
        '''Initialise BudgetManager.'''
        self.dm = dm; self.em = em
        self.budgets = self.dm.load_data("budgets", {})
        self.default_categories = self.em.categories

    def add_budget(self, name, limit, period):
        '''Adds new budget to Personal Expense Tracker.'''
        try:
            if name and limit and period:
                if name.title() not in self.budgets.keys():
                    if float(limit) > 0:
                        self.budgets[name.title()] = {"name": name.title(), "limit": float(limit), "period": period.title(), "spent": 0}
                        self.dm.save_data("budgets", self.budgets)

                        print(f"\nAdded new budget for {name.title()}: £{float(limit)}, {period.title()}")
                    else: print("Budget limit needs to be more than 0.")
                else: print(f"{name.title()} is already has a set budget.")
            else: print("Budget name, limit, and period need to be inputted!")
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
                else: print(f"{name.title()} doesn't have a set budget.")
            else: print("Budget name must be inputted!")
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
                else: return f"{name.title()} not found in budgets."
            else: return tabulate(self.budgets.values(), headers="keys", tablefmt="fancy_grid")
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
                    else: print("Deletion cancelled.")
                else: print(f"{name.title()} not found in budgets.")
            else: print("Budget name must be inputted!")
        except Exception as e:
            print(f"Error in delete_budget: {str(e)}")