import math

def isPrime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

def isPalindrome(n):
	list_of_ints = [int(i) for i in str(n)]

	size = len(list_of_ints) - 1

	palindrome = True

	for i in range(0, size):
		if list_of_ints[i] != list_of_ints[size -i]:
			palindrome = False

	return palindrome

def isPythagoreanTriplet(x,y,z):
	if x < y < z:
		if x ** 2 + y ** 2 == z ** 2:
			return True
	return False

def max(lhs, rhs):
	if lhs > rhs:
		return lhs
	else:
		return rhs

def divisorCount(n):
	limit = n
	numberOfDivisors = 1

	for i in range(1, limit):
		if(n % i == 0):
			limit = n / i
			if n == i:
				numberOfDivisors = numberOfDivisors + 1
			else:
				numberOfDivisors = numberOfDivisors + 2

	return numberOfDivisors