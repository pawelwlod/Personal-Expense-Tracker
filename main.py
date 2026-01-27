# main.py
'''Main file for Personal Expense Tracker'''

import time
from colorama import Fore
from modules import main_menu, data_manager, expense_manager, budget_manager, filter_manager, utils
utils = utils.Utils()
dm    = data_manager.DataManager()
fm    = filter_manager.FilterManager()
bm    = budget_manager.BudgetManager(dm, fm, utils)
em    = expense_manager.ExpenseManager(dm, fm, bm)
mm    = main_menu.MainMenu(dm, em, bm, utils)

is_online = True

while __name__ == '__main__' and is_online:
    try: 
        bm.spent_period(em.expenses)
        utils.header(); 
        print("\n1. Expenses\n2. Budgets\n3. Exit")

        check = False
        for name, budget in bm.budgets.items():
            if budget["options"] == "alert":
                print(Fore.RED+f"\nALERT! You have passed your {name} budget: Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}")
                check = True
            elif budget["options"] == "warn":
                print(Fore.YELLOW+f"\nWARNING! You are close to your {name} budget: Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}")
                check = True
        if not check:
            print(Fore.CYAN+"\nNo Budget Warnings/Alerts!")

        user_input = str(input(Fore.GREEN+"\nChoose an option: "))
        if user_input:
            if (user_input == "1") or (user_input.lower() == "expenses"):
                is_online = False if mm.expenses_main_menu() == "false" else True
            
            elif (user_input == "2") or (user_input.lower() == "budgets"):
                is_online = False if mm.budgets_main_menu() == "false" else True

            elif (user_input == "3") or (user_input.lower() == "exit"):
                print("Exiting...")
                dm.save_data("expenses", em.expenses)
                print("\nExpenses Saved!")

                dm.save_data("budgets", bm.budgets)
                print("\nBudgets Saved!")
                is_online = False
            else: 
                print("Invalid input!"); time.sleep(3)
    except Exception as e:
        print(f"Error in main file: {str(e)}")