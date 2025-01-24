# data_manager.py
'''Data Manager'''

import json
from datetime import datetime

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
    
    def filter_category(self, list, filter_category):
        '''Filters expenses by category'''
        try:
            filtered_list = {}
            for index, expense in list.items():    
                if expense['category'] == filter_category.title():
                    filtered_list[index] = expense
            return filtered_list
        except Exception as e:
            print(f"Error while filtering expenses by category: {str(e)}")
    

class DateManager(DataManager):
    def validate_date_range(self, start_date_input, end_date_input):
        '''Validates the date range given.'''
        try:
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
            if start_date > end_date:
                print("Error: Start date cannot be after the end date.")
                return None, None
            return start_date, end_date
        except ValueError:
            print("Error: Please enter the dates in the correct format (YYYY-MM-DD).")
            return None, None

    def filter_date_range(self, list, start_date, end_date):
        '''Filters expenses by date range'''
        try:
            filtered_expenses = {}
            for index, expense in list.items():
                try:
                    expense_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
                    if start_date <= expense_date <= end_date:
                        filtered_expenses[index] = expense
                except KeyError:
                    print(f"Skipping expense at index {index}: Missing 'date' field.")
                except ValueError:
                    print(f"Skipping expense at index {index}: Invalid date format.")
            return filtered_expenses
        except Exception as e:
            print(f"Error while filtering expenses by date: {str(e)}")
            return {}