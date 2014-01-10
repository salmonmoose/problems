import eu

length = 0
count = 0

while length < 1000:
	fib = eu.Fibonacci2(count)
	length = len(str(fib))
	count = count + 1
	print (count, fib, length)