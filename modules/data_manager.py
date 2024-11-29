# data_manager.py
'''Data Manager'''

import json

class DataManager:
    '''Manages expense data for Personal Expense Tracker.'''
    
    def save_data(self, data):
        '''Save data to file'''
        file_name = 'data/expenses.json'
        
        with open(file_name, 'a') as file:
            json.dump(data, file, indent=4, separators=(',', ': '))
            print(f"\nData saved to: {file_name} ")