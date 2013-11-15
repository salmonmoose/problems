import sys
import eu

def main(n):
	list_of_factors = {}

	n = int(n[1])

	for i in range(2, n + 1):
		if eu.isPrime(i):
			list_of_factors[i] = i

	for factor in list_of_factors:
		result = 0
		power = 1
		while result < n:
			list_of_factors[factor] = result
			result = factor ** power
			power = power + 1

	smallest_product = 1

	for factor in list_of_factors:
		smallest_product = smallest_product * list_of_factors[factor]

	print smallest_product

if __name__ == "__main__":
	main(sys.argv)