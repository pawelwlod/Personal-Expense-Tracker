# main.py
'''Main file for Personal Expense Tracker'''

import sys
import time
from colorama import Fore
import budgets, data_handler, expenses, filters, menu, utils

dm    = data_handler.DataManager("prod")
fm    = filters.FilterManager()
bm    = budgets.BudgetManager(dm, fm)
em    = expenses.ExpenseManager(dm, fm, bm)
mm    = menu.MainMenu(dm, em, bm)
utils = utils.Utils(bm)

while __name__ == '__main__':
    try: 
        utils.header(); 
        print("\n1. Expenses\n2. Budgets\n3. Exit")
        utils.budget_checks(em.expenses)

        user_input = str(input(Fore.GREEN+"\nChoose an option: ")).strip().lower()
        if user_input in ['1', 'expenses']:
            mm.expenses_main_menu()

        elif user_input in ['2', 'budgets']:
            mm.budgets_main_menu()

        elif user_input in ['3', 'exit']:
            print("Exiting...")
            for i in ['expenses', 'budgets']:
                dm.save_data(i, em.expenses) if i == 'expenses' else dm.save_data(i, bm.budgets)
                print(f"\n{i.title()} Saved!")
            sys.exit(1)
            
        else: 
            print("Invalid input!")
            time.sleep(3)
    except Exception as e:
        print(f"Error in main file: {str(e)}")