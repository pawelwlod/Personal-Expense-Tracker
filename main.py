# main.py
'''Main file for Personal Expense Tracker'''

import os
import time
import pyfiglet
from colorama import Fore
from modules import main_menu, data_manager, expense_manager, budget_manager
mm = main_menu.MainMenu()
dm = data_manager.DataManager()
em = expense_manager.ExpenseManager()
bm = budget_manager.BudgetManager()

is_online = True

def header():
    '''Header for Personal Expense Tracker.'''
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        title = pyfiglet.figlet_format("Personal Expense Tracker")
        print(Fore.GREEN+title)
    except Exception as e:
        print(f"Error in header: {str(e)}")

while __name__ == '__main__' and is_online:
    try: 
        header(); print("\n1. Expenses\n2. Budgets\n3. Exit")
        user_input = str(input("Choose an option: "))
        if user_input:
            if (user_input == "1") or (user_input.lower() == "expenses"):
                is_online = False if mm.expenses_main_menu() == "false" else True
            
            elif (user_input == "2") or (user_input.lower() == "budgets"):
                is_online = False if mm.budgets_main_menu() == "false" else True

            elif (user_input == "3") or (user_input.lower() == "exit"):
                print("Exiting...")
                dm.save_data("expenses", em.expenses); print("\nExpenses Saved!")

                dm.save_data("budgets", bm.budgets); print("\nBudgets Saved!")
                is_online = False
            else: print("Invalid input!"); time.sleep(3)
    except Exception as e:
        print(f"Error in main file: {str(e)}")