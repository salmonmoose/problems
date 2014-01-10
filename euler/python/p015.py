def LaticePath(n):
	L = [1] * n
	for i in range(n):
		for j in range(i):
			L[j] = L[j] + L[j-1]

		L[i] = 2 * L[i - 1]
	return L[n -1]
	
print LaticePath(1)
print LaticePath(2)
print LaticePath(3)
print LaticePath(20)