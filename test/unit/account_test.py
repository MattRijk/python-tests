import unittest
from bank.account import Account


class TestAccount(unittest.TestCase):

	def test_account_object_returns_current_balance(self):
		account = Account('001', 50)
		self.assertEqual(account.account_number, '001')
		self.assertEqual(account.balance, 50)

	# uniquely access the bank account and retreive the balance.
	# Bank dictionary: where key, val -> account_number, balance
	# def test_account_dict_returns_account_number_as_key_balance_as_val(self):
	# 	account = Account('001', 50)
	# 	self.assertDictEquals(account.account_number, account.balance)


if __name__ == '__main__':
	unittest.main()