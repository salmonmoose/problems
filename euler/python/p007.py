import eu

count = 0
i = 1

while count < 10001:
	i = i + 1
	if eu.isPrime(i):
		count = count + 1

print i