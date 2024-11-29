# data_manager.py
'''Data Manager'''

import json

class DataManager:
    '''Manages expense data for Personal Expense Tracker.'''
    def __init__(self):
        self.file_name = 'data/expenses.json'
    
    def save_data(self, data):
        '''Save data to file'''
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4, separators=(',', ': '))
    
    def load_data(self, default):
        '''Load data from file'''
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return default