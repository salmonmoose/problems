import eu

triangleNumber = 0

count = 1

divisorCount = 0

while divisorCount < 500:
	triangleNumber = triangleNumber + count
	count = count + 1
	divisorCount = eu.divisorCount(triangleNumber)
	print (triangleNumber, divisorCount)

print triangleNumber