# data_manager.py
'''Data Manager'''

import json

class DataManager:
    '''Manages expense data for Personal Expense Tracker.'''
    def __init__(self):
        self.file_name = 'data/expenses.json'
    
    def save_data(self, data):
        '''Save data to file'''
        try:
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4, separators=(',', ': '))
        except Exception as e:
            print(f"Error while saving expenses: {str(e)}")
    
    def load_data(self, default):
        '''Load data from file'''
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return default
        except Exception as e:
            print(f"Error while loading expenses: {str(e)}")
    
    def filter_data(self, list, filter):
        try:
            filtered_list = {}
            for index, expense in list.items():    
                if expense['category'] == filter.title():
                    filtered_list[index] = expense
            return filtered_list
        except Exception as e:
            print(f"Error while filtering expenses: {str(e)}")