# main_menu.py
'''Main Menu'''

import os
import pyfiglet
from colorama import Fore
import time
from datetime import datetime
from modules import expense_manager, data_manager, budget_manager
em = expense_manager.ExpenseManager()
dm = data_manager.DataManager()
bm = budget_manager.BudgetManager()

class MainMenu:
    '''Main Menu for Personal Expense Tracker.'''

    def header(self):
        '''Header for Personal Expense Tracker.'''
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            title = pyfiglet.figlet_format("Personal Expense Tracker")
            print(Fore.GREEN+title)
        except Exception as e:
            print(f"Error in header: {str(e)}")

    def exit(self):
        '''Exits Expense Tracker.'''

        print("Exiting...")
        dm.save_data("expenses", em.expenses)
        print("\nExpenses Saved!")
        dm.save_data("budgets", bm.budgets)
        print("\nBudgets Saved!")

        return "false" 

    def expenses_main_menu(self):
        '''The expense main menu for the Personal Expense Tracker.'''
        while True:
            try:
                mm = MainMenu()
                mm.header()
                print("\n1. Add Expense\n2. Display Expenses\n3. Exit")
                expense_user_input = str(input("Choose an option: "))

                if expense_user_input:
                    if (expense_user_input == '1') or (expense_user_input.lower() == 'add expense'):
                        print("\nSend 'exit' in any of the fields to cancel.")
                        date = str(input("Enter date (YYYY-MM-DD): ")).strip()
                        if date == 'exit':
                            continue
                        try:
                            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                        except ValueError:
                            print("Invalid date format. Please enter the date in YYYY-MM-DD format or type 'exit' to return.")
                        amount = str(input("Enter expense amount (format: £0.00): "))
                        if amount == 'exit':
                            continue
                        category = str(input(f"Enter category ({' '.join(str(e.title()) for e in em.categories)}): "))
                        if category == 'exit':
                            continue
                        em.add_expense(amount=amount, category=category, date=str(parsed_date))
                        time.sleep(3)

                    elif (expense_user_input == '2') or (expense_user_input.lower() == 'display expenses'):
                        print(em.display_expenses())
                        time.sleep(5)

                    elif (expense_user_input.lower() == 'exit') or (expense_user_input == '3'):
                        return mm.exit()

                    else:
                        print(f"Invalid input! Please try again.")
                        time.sleep(3)
            except Exception as e:
                print(f"Error in expenses_main_menu: {str(e)}")
    
    def budgets_main_menu(self):
        '''The budget main menu for the Personal Expense Tracker.'''
        while True:
            try:
                mm = MainMenu()
                mm.header()
                print("\n1. Add Budget\n2. Edit Budget\n3. Display Budgets\n4. Delete Budget\n5. Exit")
                budget_user_input = str(input("Choose your option: "))

                if budget_user_input:
                    if (budget_user_input == '1') or (budget_user_input.lower() == 'add budget'):
                        print("\nSend 'exit' in any of the fields to cancel.")
                        budget_name = str(input("Enter budget name: ")).strip()
                        if budget_name.lower() == 'exit':
                            continue
                        budget_limit = str(input("Enter budget limit: "))
                        if budget_limit.lower() == 'exit':
                            continue
                        budget_period = str(input("Enter budget period: (Weekly, Monthly, Yearly) "))
                        if budget_period.lower() == 'exit':
                            continue
                        
                        bm.add_budget(budget_name, budget_limit, budget_period)
                        time.sleep(3)
                    
                    elif (budget_user_input == '2') or (budget_user_input.lower() == 'edit budget'):
                        print("\nSend 'exit' in any of the fields to cancel.")
                        choice = str(input("Would you like to edit the name or period?: "))
                        name, value = str(input("Enter budget name: ")).strip()
                        if name.lower() == 'exit':
                            continue
                        if choice.lower() == 'period':
                            value = str(input("Enter budget period: "))
                            if value.lower() == 'exit':
                                continue
                        else:
                            print("Enter a valid option!")
                            continue

                        bm.edit_budget(choice, name, value)
                        time.sleep(3)
                    
                    elif (budget_user_input == '3') or (budget_user_input.lower() == 'display budgets'):
                        print(bm.display_budgets())
                        time.sleep(5)
                    
                    elif (budget_user_input == '4') or (budget_user_input.lower() == 'delete budget'):
                        print("\nSend 'exit' in any of the fields to cancel.")
                        budget_name = str(input("Enter budget name: ")).strip()
                        if budget_name.lower() == 'exit':
                            continue

                        bm.delete_budget(budget_name)
                        time.sleep(3)

                    elif (budget_user_input == '5') or (budget_user_input.lower() == 'exit'):
                        return mm.exit()
                    
                    else:
                        print(f"Invalid input! Please try again.")
                        time.sleep(3)
            except Exception as e:
                print(f"Error in budgets_main_menu: {str(e)}")