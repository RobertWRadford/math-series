from math_series.math_series import fibonacci, lucas, sum_series

def test_fibonacci():
	actual = fibonacci(3)
	expect = 2
	assert actual == expect

def test_lucas():
	actual = lucas(3)
	expect = 4
	assert actual == expect

def test_sum_series():
	actual = sum_series(3)
	expect = 2
	assert actual == expect, 'first assert'
	actual = sum_series(2, 5, 3)
	expect = 8
	assert actual == expect, 'second assert'