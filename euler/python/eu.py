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

def sumOfDigits(n):
	list_of_ints = [int(i) for i in str(n)]

	sum_of_ints = 0

	for i in range(0, len(list_of_ints)):
		sum_of_ints = sum_of_ints + list_of_ints[i]

	return sum_of_ints


def divisorCount(n):
	limit = n
	numberOfDivisors = 1

	for i in range(1, limit):
		if(n % i == 0):
			numberOfDivisors = numberOfDivisors + 1

	return numberOfDivisors

def intToString(n):
	list_of_ints = [int(i) for i in str(n)]
	string = ''

	digits = [
		'','one','two','three','four','five','six','seven','eight','nine',
		'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
	]

	tens = [
		'','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'
	]

	if len(list_of_ints) > 3 and list_of_ints[-4] > 0:
		string = string + digits[list_of_ints[-4]]+'thousand'

	if len(list_of_ints) > 2 and list_of_ints[-3] > 0:
		string = string + digits[list_of_ints[-3]] + 'hundred'

	if string != '':
		if list_of_ints[-2] > 0 or list_of_ints[-1] > 0:
			string = string + "and"


	if len(list_of_ints) > 1:
		if list_of_ints[-2] > 1:
			string = string + tens[list_of_ints[-2]]
			string = string + digits[list_of_ints[-1]]
		elif list_of_ints[-2] == 1:
			string = string + digits[list_of_ints[-2] * 10 + list_of_ints[-1]]
		else:
			string = string + digits[list_of_ints[-1]]
	else:
		string = string + digits[list_of_ints[-1]]

	return string