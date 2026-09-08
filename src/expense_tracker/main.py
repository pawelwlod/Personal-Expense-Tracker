# main.py
'''Main file for Personal Expense Tracker'''

from tkinter import *
from tkinter import ttk
import budgets, data_handler, expenses, filters, menu, utils

dm    = data_handler.DataManager("prod")
fm    = filters.FilterManager()
bm    = budgets.BudgetManager(dm, fm)
em    = expenses.ExpenseManager(dm, fm, bm)
mm    = menu.MainMenu(dm, em, bm)
utils = utils.Utils(bm)

class MainMenu:
    def __init__(self, root):
        self.mainframe = ttk.Frame(root)
        root.title("Personal Expense Tracker")
        self.mainframe.place(relx=0.5, rely=0.5, anchor="center")

        self.budget_checks = utils.budget_checks(em.expenses)
        row = 0

        ttk.Label(
            self.mainframe, text="Personal Expense Tracker", font=('Arial', 16)
        ).grid(column=0, row=row)
        row += 1

        for message in self.budget_checks:
            ttk.Label(
                self.mainframe, text=message, font=("Arial", 12)
            ).grid(column=0, row=row)
            row += 1

        ttk.Button(
            self.mainframe, text="Expenses", width=20, command=mm.expenses_main_menu
        ).grid(column=0, row=row)
        row += 1

        ttk.Button(
            self.mainframe, text="Budgets", width=20, command=mm.budgets_main_menu
        ).grid(column=0, row=row)
        row += 1

        ttk.Button(
            self.mainframe, text="Exit", width=20, command=self.close_application
        ).grid(column=0, row=row)
        row += 1

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=20, pady=20)

    def close_application(self):
        print("Exiting...")
        dm.save_data("expenses", em.expenses)
        print("Expenses Saved!")

        dm.save_data("budgets", bm.budgets)
        print("Budgets Saved!")

        root.destroy()
        
root = Tk()
root.geometry("1920x1080")
MainMenu(root)
root.mainloop()