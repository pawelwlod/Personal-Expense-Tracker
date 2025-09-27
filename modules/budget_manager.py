# budget_manager.py
'''Budget Manager'''

from modules import data_manager
dm = data_manager.DataManager()

class BudgetManager:
    '''Manages budgets for Personal Expense Tracker'''
    def __init__(self):
        '''Initialise BudgetManager.'''
        self.budgets = dm.load_data(type="budgets", default={})

    