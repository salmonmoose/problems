def Collatz(n):
	if (n % 2 == 0):
		return n / 2
	else:
		return n * 3 + 1

def GetColltzChain(value):
	count = 1;

	while value > 1:
		value = Collatz(value)
		count = count + 1

	return count

largest = 0
start = 0

for i in range(999999, 1, -1):
	chain = GetColltzChain(i)
	print (i, chain)
	if chain > largest:
		largest = chain
		start = i

print (start, largest)