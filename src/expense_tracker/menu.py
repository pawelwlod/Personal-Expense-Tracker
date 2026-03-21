# Menu.py
'''Main Menu'''

import time
from datetime import datetime
from colorama import Fore
from . import utils

class MainMenu:
    '''Main Menu for Personal Expense Tracker.'''
    def __init__(self, dm, em, bm):
        '''Initialises MainMenu.'''
        self.dm    = dm
        self.em    = em
        self.bm    = bm
        self.utils = utils.Utils(bm)

    def expenses_main_menu(self):
        '''The expense main menu for the Personal Expense Tracker.'''
        while True:
            try:
                self.utils.header()
                print("\n1. Add Expense\n2. Display Expenses\n3. Exit")
                self.utils.budget_checks(self.em.expenses)

                expense_user_input = str(input(Fore.GREEN+"\nChoose an option: "))

                if expense_user_input:
                    if (expense_user_input == '1') or (expense_user_input.lower() == 'add expense'):
                        self.utils.header()
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
                        
                        category = str(input(f"Enter category ({' '.join(str(e.title()) for e in self.em.categories)}): "))
                        if category == 'exit': 
                            continue
                        
                        self.em.add_expense(amount=amount, category=category, date=str(parsed_date))
                        time.sleep(3)

                    elif (expense_user_input == '2') or (expense_user_input.lower() == 'display expenses'):
                        self.utils.header()
                        print(self.em.display_expenses())
                        time.sleep(5)

                    elif (expense_user_input.lower() == 'exit') or (expense_user_input == '3'): 
                        return "true"

                    else: 
                        print(f"Invalid input! Please try again.")
                        time.sleep(3)
            except Exception as e:
                print(f"Error in expenses_main_menu: {str(e)}")
    
    def budgets_main_menu(self):
        '''The budget main menu for the Personal Expense Tracker.'''
        while True:
            try:
                self.utils.header()
                print("\n1. Add Budget\n2. Edit Budget\n3. Display Budgets\n4. Delete Budget\n5. Exit")
                self.utils.budget_checks(self.em.expenses)

                budget_user_input = str(input(Fore.GREEN+"\nChoose your option: "))

                if budget_user_input:
                    if (budget_user_input == '1') or (budget_user_input.lower() == 'add budget'):
                        self.utils.header()
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
                        
                        self.bm.add_budget(budget_name, budget_limit, budget_period)
                        time.sleep(3)
                    
                    elif (budget_user_input == '2') or (budget_user_input.lower() == 'edit budget'):
                        self.utils.header()
                        print("\nSend 'exit' in any of the fields to cancel.")
                        choice = str(input("Would you like to edit the budget amount or period?: "))
                        if choice.lower() == 'exit':
                            continue

                        name = str(input("Enter budget name: ")).strip()
                        if name.lower() == 'exit': 
                            continue
                        
                        if choice.lower() == 'period':
                            value = str(input("Enter budget period: "))
                            if value.lower() == 'exit': 
                                continue
                        
                        elif choice.lower() == 'amount':
                            value = str(input("Enter budget amount: "))
                            if value.lower() == 'exit' : 
                                continue
                        
                        else:
                            print("Enter a valid option!")
                            time.sleep(3)
                            continue

                        self.bm.edit_budget(choice, name, value)
                        time.sleep(3)
                    
                    elif (budget_user_input == '3') or (budget_user_input.lower() == 'display budgets'):
                        self.utils.header()
                        print(self.bm.display_budgets())
                        time.sleep(5)
                    
                    elif (budget_user_input == '4') or (budget_user_input.lower() == 'delete budget'):
                        self.utils.header()
                        print("\nSend 'exit' in any of the fields to cancel.")
                        budget_name = str(input("Enter budget name: ")).strip()
                        if budget_name.lower() == 'exit': 
                            continue

                        self.bm.delete_budget(budget_name)
                        time.sleep(3)

                    elif (budget_user_input == '5') or (budget_user_input.lower() == 'exit'): 
                        return "true"
                    
                    else:
                        print(f"Invalid input! Please try again.")
                        time.sleep(3)
            except Exception as e:
                print(f"Error in budgets_main_menu: {str(e)}")