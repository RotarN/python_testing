import unittest
from unittest.mock import Mock, patch

import file_search


class TestSearch(unittest.TestCase):
	def test_search(self):
		file_search.read = Mock()
		file_search.read.return_value = "Happy flow"
		result = file_search.search_text_in_file('Happy', 'orice.txt')
		self.assertEqual(result, 1)

	@patch('file_search.read')
	def test_search_decorator(self, mock_read):
		mock_read.return_value = "happy flow happy."
		result = file_search.search_text_in_file('Happy', 'orice.txt')
		self.assertEqual(result, 0)

	def test_search_with(self):
		with patch('file_search.read') as mock_read:
			mock_read.return_value = "happy flow happy."
			result = file_search.search_text_in_file('Happy', 'orice.txt')
			self.assertEqual(result, 0)