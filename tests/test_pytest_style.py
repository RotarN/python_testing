import pytest

from custom_sum import custom_sum


def test_sum_list():
	assert custom_sum(2, 3, 12, 11,) == 28, 'not valid'


def test_sum_fail():
	with pytest.raises(TypeError):
		assert custom_sum(2, 3, 12, 11, 'abc') == 28, 'not valid'
