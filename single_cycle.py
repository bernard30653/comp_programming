# This is a question from algoexpert Single Cycle Check
# Given an array where each element represent the number of jumps(i.e. 2 means 2 indices forward
# and -4 means 4 indices backward
# Check if an input array is such that there is a single cycle
def hasSingleCycle(array):
    # Write your code here.
    arrLen = len(array)
    elemVisited = 0
	currIdx = 0
	while elemVisited < arrLen:
		if array[currIdx] ==0:
			return False
		if elemVisited > 0 and currIdx == 0:
			return False
		currIdx = (currIdx+array[currIdx])%arrLen
		elemVisited +=1
	if currIdx !=0:
		return False
	return True
