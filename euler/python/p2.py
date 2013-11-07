previous = 1
current = 1
count = 0

while current < 4000000:
	if (current % 2) == 0:
		count = count + current
	print(current)
	temp = current
	current = previous + current
	previous = temp

print(count)