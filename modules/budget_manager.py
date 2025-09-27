# budget_manager.py
'''Budget Manager'''

from modules import data_manager
dm = data_manager.DataManager()

class BudgetManager:
    '''Manages budgets for Personal Expense Tracker'''
    def __init__(self):
        '''Initialise BudgetManager.'''
        self.budgets = dm.load_data(type="budgets", default={})

    def add_budget(self, name, limit):
        '''Adds new budget to Personal Expense Tracker.'''
        pass

    def edit_budget(self, name):
        '''Edits existing budget in Personal Expense Tracker.'''
        pass

    def display_budgets(self):
        '''Displays all or filtered budgets.'''
        pass

    def delete_budget(self, name):
        '''Deletes existing budget from Personal Expense Tracker.'''
        pass