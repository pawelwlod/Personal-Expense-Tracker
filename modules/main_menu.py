# main_menu.py
'''Main Menu'''

import time
import os
import pyfiglet
from colorama import Fore
from datetime import datetime
from modules import expense_manager, data_manager, budget_manager
em = expense_manager.ExpenseManager()
dm = data_manager.DataManager()
bm = budget_manager.BudgetManager()

def main_menu(is_online):
    '''The main menu for the Personal Expense Tracker.'''
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            title = pyfiglet.figlet_format("Personal Expense Tracker")
            print(Fore.GREEN+title)

            print("\n1. Add Expense\n2. Display Expenses\n3. Exit")
            user_input = str(input("Choose an option: "))

            if user_input:
                if (user_input == '1') or (user_input.lower() == 'add expense'):
                    print("\nSend 'exit' in any of the fields to cancel.")
                    date = str(input("Enter date (YYYY-MM-DD): ")).strip()
                    if date == 'exit':
                        return exit(is_online)
                    try:
                        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format or type 'exit' to return.")
                    amount = str(input("Enter expense amount (format: £0.00): "))
                    if amount == 'exit':
                        return exit(is_online)
                    category = str(input(f"Enter category ({' '.join(str(e.title()) for e in em.categories)}): "))
                    if category == 'exit':
                        return exit(is_online)

                    em.add_expense(amount=amount, category=category, date=str(parsed_date))
                    time.sleep(3)

                elif (user_input == '2') or (user_input.lower() == 'display expenses'):
                    print(em.display_expenses())
                    time.sleep(5)

                elif (user_input.lower() == 'exit') or (user_input == '3'):
                    return exit(is_online)

                else:
                    print(f"Invalid input! Please try again.")
                    time.sleep(3)
        except Exception as e:
            print(f"Error in main_menu: {str(e)}")

def exit(is_online):
    '''Exits Expense Tracker.'''
    
    print("Exiting...")
    dm.save_data("expenses", em.expenses)
    print("\nExpenses Saved!")

    is_online = False
    return is_online 