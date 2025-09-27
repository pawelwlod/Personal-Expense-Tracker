# filter_manager.py
'''Filter Manager'''

from datetime import datetime
from modules import data_manager
dm = data_manager.DataManager()

class FilterManager:
    '''Manages expense filtering for Personal Expense Tracker.'''
    def __init__(self):
        '''Initialise FilterManager.'''
        self.categories = ['food', 'transport', 'entertainments', 'utilities', 'custom']
        self.expenses = dm.load_data(type="expenses", default={})

    def filter_data(self, type):
        '''Filters expenses by either a category or amount range.'''
        try:
            filtered_list = {}
            if type.lower() == "category":
                filter = str(input(f"Filter by category: ({' '.join(str(e.title()) for e in self.categories)}) "))
                for index, expense in self.expenses.items():
                    if expense['category'] == filter.title():
                        filtered_list[index] = expense
            else:
                start_amount, end_amount = float(input("Enter start amount: ")), float(input("Enter end amount: "))
                for index, expense in self.expenses.items():
                    if start_amount < end_amount:
                        if expense['amount'] >= start_amount and expense['amount'] <= end_amount:
                            filtered_list[index] = expense
                    else:
                        print("Start amount cannot be bigger than end amount.")
            return filtered_list
        except Exception as e:
            print(f"Error while filtering expenses by category/amount: {str(e)}")
            return {}

    def filter_date_range(self, start_date, end_date):
        '''Filters expenses by date range'''
        try:
            filtered_expenses = {}
            for index, expense in self.expenses.items():
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
    
    def filter_multiple(self, mul_filters):
        '''Filters expenses by more than one filter.'''
        try:
            filtered_expenses, temp_expenses, temp_expenses_2 = {}, {}, {}
            for filter in mul_filters:
                if filter != 'date':
                    filtered_list = FilterManager.filter_data(self=self, type=filter)                   
                else:
                    start_date = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
                    end_date = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d").date()
                    filtered_list = FilterManager.filter_date_range(self, start_date, end_date)
                    
                if not temp_expenses:
                    for index, expense in filtered_list.items():
                        temp_expenses[index] = expense
                elif not temp_expenses_2:
                    for index, expense in filtered_list.items():
                        for temp_index, temp_expense in temp_expenses.items():
                            if temp_index == index:
                                temp_expenses_2[temp_index] = temp_expense
                else:
                    for index, expense in filtered_list.items():                        
                        for temp2_index, temp2_expense in temp_expenses_2.items():
                            if temp2_index == index:
                                filtered_expenses[temp2_index] = temp2_expense
            if not filtered_expenses:
                return temp_expenses_2
            else:
                return filtered_expenses
        except Exception as e:
            print(f"Error while filtering expenses by multiple filters: {str(e)}")
            return {}