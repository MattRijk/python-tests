import unittest
from bank.account import Account
from bank.bank import Bank


class TestAccount(unittest.TestCase):

	def setUp(self):
		self.bank = Bank()
		self.account_1 = Account(001, 50)
		self.account_2 = Account(002, 100)

	def test_bank_is_initially_empty(self):
	   
	    self.assertEqual({}, self.bank.accounts)
	    self.assertEqual(len(self.bank.accounts), 0)

	def test_add_account(self):
		# bank = Bank()


		self.bank.add_account(self.account_1)
		self.bank.add_account(self.account_2)

		self.assertEqual(len(self.bank.accounts), 2)

	def test_get_account_balance(self):
		# bank = Bank()

		# self.account_1 = Account(001, 50)

		self.bank.add_account(self.account_1)

		self.assertEqual(self.bank.get_account_balance(001), 50)

if __name__ == '__main__':
	unittest.main()

