# main.py
'''Main file for Personal Expense Tracker'''
from modules import main_menu

is_online = True
    
if __name__ == '__main__' and is_online:
    is_online = main_menu.main_menu(is_online)