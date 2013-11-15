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