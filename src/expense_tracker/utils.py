# utils.py
'''Utils Functions'''

class Utils:
    '''Contains util functions for Personal Expense Tracker.'''
    def __init__(self, bm):
        '''Initialises Utils.'''
        self.bm = bm
    
    def budget_checks(self, expenses: dict):
        '''Checks budgets and returns any relevant alerts/warning.'''
        try:
            self.bm.spent_period(expenses)
            check = False
            for name, budget in self.bm.budgets.items():
                if budget["options"] == "alert":
                    print(f"\nALERT! You have passed your {budget["period"]} {name} budget: Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}")
                    check = True
                elif budget["options"] == "warn":
                    print(f"\nWARNING! You are close to your {budget["period"]} {name} budget: Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}")
                    check = True
            if not check:
                print("\nNo Budget Warnings/Alerts!")
        except Exception as e:
            print(f"Error in budget_checks: {str(e)}")

    def budget_message(self, name, budget: dict):
        '''Creates message for each relevant budget alert/warning.'''
        try:
            message = ''
            if budget["options"] == "alert":
                message = f'''ALERT! You have passed your {budget["period"]} {name} budget: 
                Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}'''

            elif budget["options"] == "warn":
                message = f'''WARNING! You are close to your {budget["period"]} {name} budget:
                Spent - £{budget["spent"]}, Remaining - £{budget["remaining"]}'''

            return message
        except Exception as e:
            return f"Error in budget_message: {str(e)}"