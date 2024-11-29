import sys
sys.path.insert(0, 'modules')
from expense_manager import ExpenseManager
import unittest

class ExpenseManagerTest(unittest.TestCase):
    '''Tests for the ExpenseManager.'''
    def test_adding_expense(self):
        '''Test for adding an expense to the ExpenseManager.'''
        expense_manager = ExpenseManager()
        date = '2024-11-29'
        expense_manager.add_expense(amount=5.50,category='Food',date=date)
        self.assertEqual(5.5, expense_manager.expenses[date]['amount'])
        self.assertEqual('Food', expense_manager.expenses[date]['category'])

if __name__ == '__main__':
    unittest.main()