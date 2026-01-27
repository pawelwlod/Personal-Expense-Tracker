# DataHandler.py
'''Data Handler'''

import json
import os
from pathlib import Path

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class DataManager:
    '''Manages expense and budget data for Personal Expense Tracker.'''
    def __init__(self):
        self.expense_file_name = Path(CURRENT_DIR) / 'expenses.json'
        self.budget_file_name  = Path(CURRENT_DIR) / 'budgets.json'

    def save_data(self, type, data):
        '''Save data to file'''
        try:
            if type == "expenses".lower():
                with open(self.expense_file_name, 'w') as file:
                    json.dump(data, file, indent=4, separators=(',', ': '))
            else:
                with open(self.budget_file_name, 'w') as file:
                    json.dump(data, file, indent=4, separators=(',', ': '))
        except Exception as e:
            print(f"Error while saving expenses: {str(e)}")
    
    def load_data(self, type, default):
        '''Load data from file'''
        try:
            if type == "expenses".lower():
                with open(self.expense_file_name, 'r') as file:
                    return json.load(file)
            else:
                with open(self.budget_file_name, 'r') as file:
                    return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return default
        except Exception as e:
            print(f"Error while loading expenses: {str(e)}")