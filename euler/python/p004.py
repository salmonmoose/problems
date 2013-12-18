import eu

palindrome = 0
lhs = 999
rhs = 999

while lhs > 99 and rhs > 99:
	product = lhs * rhs
	if eu.isPalindrome(product) and product > palindrome:
		palindrome = product
	rhs = rhs -1
	if rhs < lhs:
		rhs = 999
		lhs = lhs -1

print palindrome