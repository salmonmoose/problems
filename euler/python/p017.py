import eu

sum_of_numbers = 0

for i in range(1000 + 1):
	number = eu.intToString(i)
	sum_of_numbers = sum_of_numbers + len(number)
	print (i,eu.intToString(i), len(number), sum_of_numbers)
