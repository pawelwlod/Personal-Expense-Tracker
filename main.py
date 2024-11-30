# main.py

import time
import pyfiglet
import os
import sys
sys.path.insert(0, 'modules')
from expense_manager import ExpenseManager          # type: ignore

expense_manager = ExpenseManager()
online = True

def main_menu():
    '''The main menu for the Personal Expense Tracker.'''
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pyfiglet.figlet_format("Personal Expense Tracker"))

        print("\n1. Add Expense\n2. Display Expenses\n3. Exit")
        user_input = str(input("Choose an option: "))

        if user_input:
            if (user_input == '1') or (user_input.lower() == 'add expense'):
                date = str(input("\nEnter date (YYYY-MM-DD): "))
                amount = float(input("Enter expense amount (format: £0.00): "))
                category = str(input("Enter category (Food, Transport, Games, Other): "))

                expense_manager.add_expense(amount=amount, category=category, date=date)
                time.sleep(3)
            
            elif (user_input == '2') or (user_input.lower() == 'display expenses'):
                print(expense_manager.display_expenses())
                time.sleep(5)

            elif (user_input.lower() != 'exit') or (user_input != '3'):
                print("Exiting...")
                global online
                online = False

                break
            
            else:
                print(f"Invalid input! Please try again.")
                time.sleep(3)
    
if __name__ == '__main__':
    while online == True:
        main_menu()