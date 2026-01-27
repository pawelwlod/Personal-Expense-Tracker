# utils.py
'''Utils Functions'''

import os
import pyfiglet
from colorama import Fore

class Utils:
    '''Contains util functions for Personal Expense Tracker.'''
    def header(self):
        '''Header for Personal Expense Tracker.'''
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            title = pyfiglet.figlet_format("Personal Expense Tracker")
            print(Fore.GREEN+title)
        except Exception as e:
            print(f"Error in header: {str(e)}")