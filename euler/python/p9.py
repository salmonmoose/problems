import eu

for y in range (1, 1001):
	for x in range (1, y):
		if x + y < 1000:
			z = 1000 - x - y
			if eu.isPythagoreanTriplet(x,y,z):
				print (x * y * z)