# utils.py
'''Utils Functions'''

import os
import pyfiglet
from colorama import Fore

class Utils:
    '''Contains util functions for Personal Expense Tracker.'''
    def __init__(self, bm):
        '''Initialises Utils.'''
        self.bm = bm
    
    def header(self):
        '''Header for Personal Expense Tracker.'''
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            title = pyfiglet.figlet_format("Personal Expense Tracker")
            print(Fore.GREEN+title)
        except Exception as e:
            print(f"Error in header: {str(e)}")
    
    def budget_checks(self, expenses):
        '''Checks budgets and returns any relevant alerts/warning.'''
        try:
            self.bm.spent_period(expenses)
            check = False
            for name, budget in self.bm.budgets.items():
                if budget["options"] == "alert":
                    print(Fore.RED+f"\nALERT! You have passed your {budget["period"]} {name} budget: Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}")
                    check = True
                elif budget["options"] == "warn":
                    print(Fore.YELLOW+f"\nWARNING! You are close to your {budget["period"]} {name} budget: Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}")
                    check = True
            if not check:
                print(Fore.CYAN+"\nNo Budget Warnings/Alerts!")
        except Exception as e:
            print(f"Error in budget_checks: {str(e)}")