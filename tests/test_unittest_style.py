import unittest

from custom_sum import custom_sum


class TestCustomSum(unittest.TestCase):
	def test_sum_list(self):
		# actual = custom_sum(1, 2, 10)
		# expected = 13
		# self.assertEquals(actual, expected)
		self.assertEqual(custom_sum(1, 2, 10, [5, 4]), 22, 'not valid')

	def test_sum_mixt(self):
		self.assertEqual(custom_sum(1.9, 2.2, 1.5, [[2.3, 21.2]], 32), 61.1)

	def test_sum_fail(self):
		with self.assertRaises(TypeError):
			self.assertEqual(custom_sum(1.9, 2.2, 1.5, [[2.3, 21.2]], 32, "abc"), 61.1)
