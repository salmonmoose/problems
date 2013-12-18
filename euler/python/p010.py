import eu

count = 2
sumOfPrimes = 0

while count < 2000000:
	if eu.isPrime(count):
		sumOfPrimes = sumOfPrimes + count
	count = count + 1

print sumOfPrimes