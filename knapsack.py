'''
Algoexpert.io knapsack problem
Sample Input:
items = [[1,2],[4,3],[5,6],[6,7]]
capacity = 10
Sample Output:
[10,[1,3]] // items [4,3] and [6,7]
'''
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
	itemIndices = []
	nItems = len(items)
	values = list(map(lambda x:x[0], items))
	weights = list(map(lambda x:x[1], items))
	booleanArr = [[False for c in range(capacity+1)] for i in range(nItems+1)]
	ansTable = [[0 for c in range(capacity+1)] for i in range(nItems+1)]
	# ansTable[i][j]:== The maximum value given the items {1,...,i} with a constraint of j
	for i in range(1,nItems+1):
		for c in range(1,capacity+1):
			if weights[i-1]> c or ansTable[i-1][c] > values[i-1]+ansTable[i-1][c-weights[i-1]]:
				ansTable[i][c] = ansTable[i-1][c]
				'''
				# We will not take the i-th item if
				  1.The weight of it is bigger than the capacity
				  2.Not taking the i-th item if this yields a bigger weight
				'''
			else:
				booleanArr[i][c] = True
				ansTable[i][c] = values[i-1]+ansTable[i-1][c-weights[i-1]]
	maxValue = ansTable[nItems][capacity]
	tempCapacity = capacity
	for i in range(nItems,0,-1):
		if booleanArr[i][tempCapacity]==True: # The case where we take (i-1)th item
			itemIndices =  [i-1]+itemIndices
			tempCapacity = tempCapacity-weights[i-1]
	return [maxValue,itemIndices]
