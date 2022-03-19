import datetime
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import age_calculator


class ContainersTestCase(unittest.TestCase):

	def setUp(self):
		self.response = io.StringIO()

	def test_get_dob(self):
		today = datetime.date.today()
		user_input = [today.year, today.month, today.day]
		with patch('builtins.input', side_effect=user_input):
			dob = age_calculator.get_dob()
			self.assertTrue(dob == today)

	def test_get_age(self):
		dob = datetime.date(1990, 4, 1)
		age = int(age_calculator.get_age(dob))

		today = datetime.date.today()
		expected = (today - dob).days // 365

		self.assertTrue(age == expected)

	def test_main_invalid(self):
		date = datetime.date.today() + datetime.timedelta(days=1)
		user_input = [date.year, date.month, date.day]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				age_calculator.main()
				self.assertFalse("0" in self.response.getvalue())

	def test_main_valid(self):
		user_input = ['2000','1','1']
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				age_calculator.main()
				birthdate = datetime.date(2000, 1, 1)
				today = datetime.date.today()
				age = int((today - birthdate).days/365)
				self.assertTrue(str(age) in self.response.getvalue())


if __name__ == '__main__':
	unittest.main()




