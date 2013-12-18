import eu

def largestPrimeFactor(n):
	i = 2
	found = False

	while not found:
		if n % i == 0:
			factor = n / i
			found = eu.isPrime(factor)
		i = i + 1

	return factor

print largestPrimeFactor(600851475143)