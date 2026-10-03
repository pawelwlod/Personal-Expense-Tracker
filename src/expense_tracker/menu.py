# Menu.py
'''Main Menu'''

import time
from datetime import datetime
from colorama import Fore
import utils

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

                expense_user_input = str(input(Fore.GREEN+"\nChoose an option: ")).strip().lower()

                if expense_user_input in ['3', 'exit']:
                    return
                
                elif expense_user_input in ['1', 'add expense']:
                    self.utils.header()
                    print("\nSend 'exit' in any of the fields to cancel.")
                    date = str(input("Enter date (YYYY-MM-DD): ")).strip().lower()
                    if date == 'exit': 
                        continue

                    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                    
                    amount = str(input("Enter expense amount (format: £0.00): ")).strip().lower()
                    if amount == 'exit': 
                        continue
                    
                    category = str(input(f"Enter category ({' '.join(str(e.title()) for e in self.em.categories)}): ")).strip().title()
                    if category == 'exit': 
                        continue
                    
                    print(self.em.add_expense(amount=float(amount), category=category, date=str(parsed_date)))
                    time.sleep(3)

                elif expense_user_input in ['2', 'display expenses']:
                    self.utils.header()
                    print(self.em.display_expenses())
                    time.sleep(5)

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

                budget_user_input = str(input(Fore.GREEN+"\nChoose your option: ")).strip().lower()

                if budget_user_input in ['5', 'exit']:
                    return
            
                elif budget_user_input in ['1', 'add budget']:
                    self.utils.header()
                    print("\nSend 'exit' in any of the fields to cancel.")
                    
                    budget_name = str(input("Enter budget name: ")).strip()
                    if budget_name.lower() == 'exit': 
                        continue
                    
                    budget_limit = str(input("Enter budget limit: ")).strip()
                    if budget_limit.lower() == 'exit': 
                        continue
                    
                    budget_period = str(input("Enter budget period: (Weekly, Monthly, Yearly) ")).strip()
                    if budget_period.lower() == 'exit': 
                        continue 
                    
                    self.bm.add_budget(budget_name, budget_limit, budget_period)
                    time.sleep(3)
                
                elif budget_user_input in ['2', 'edit budget']:
                    self.utils.header()
                    print("\nSend 'exit' in any of the fields to cancel.")
                    choice = str(input("Would you like to edit the budget amount or period?: ")).strip().lower()
                    if choice.lower() == 'exit':
                        continue

                    name = str(input("Enter budget name: ")).strip()
                    if name.lower() == 'exit': 
                        continue
                    
                    if choice in ['period', 'amount']:
                        value = str(input(f"Enter budget {choice}: ")).strip()
                        if value.lower() == 'exit':
                            continue
                    
                    else:
                        print("Enter a valid option!")
                        time.sleep(3)
                        continue

                    self.bm.edit_budget(choice, name, value)
                    time.sleep(3)
                    
                elif budget_user_input in ['3', 'display budgets']:
                    self.utils.header()
                    print(self.bm.display_budgets())
                    time.sleep(5)
                
                elif budget_user_input in ['4', 'delete budget']:
                    self.utils.header()
                    print("\nSend 'exit' in any of the fields to cancel.")
                    budget_name = str(input("Enter budget name: ")).strip()
                    if budget_name.lower() == 'exit': 
                        continue

                    self.bm.delete_budget(budget_name)
                    time.sleep(3)
                
                else:
                    print(f"Invalid input! Please try again.")
                    time.sleep(3)
            except Exception as e:
                print(f"Error in budgets_main_menu: {str(e)}")