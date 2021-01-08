def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    # We first declare an array with a length of n
	resultArr = [0 for elem in range(n+1)]
	resultArr[0] = 0
	for i in range(1,n+1):
		temp = float('inf')
		for d in denoms:
			if i<d:
				continue
			if resultArr[i-d]<temp:
				temp = resultArr[i-d]

		resultArr[i] = temp+1
	if resultArr[-1] ==float('inf'):
		return -1
	return resultArr[-1]
