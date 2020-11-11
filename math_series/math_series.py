
def fibonacci(n):
	"""This functions is intended to return the nth position of a fibonacci sequence
	It takes in an integer value and calculates the value iteratively"""
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a+b
	return a

def lucas(n):
	"""This functions is intended to return the nth position of a lucas sequence
	It takes in an integer value and calculates the value iteratively"""
	a, b = 2, 1
	for i in range(0, n):
		a, b = b, a+b
	return a

def sum_series(n, optOne=0, optTwo=1):
	"""This functions is intended to return the nth position of a fiboncci-esque sequence
	It takes in an integer value for the position in the sequence and optionally two initial values
	without optional values it defaults to a fibonacci with 0, 1 origin
	it then uses the initial valeus to calculate the value iteratively"""
	for i in range(0, n):
		optOne, optTwo = optTwo, optOne+optTwo
	return optOne

if __name__ == '__main__':
	help(fibonacci)