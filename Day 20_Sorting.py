#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
totalSwaps = 0

for i in range(n):
    numSwaps = 0
    for j in range(n-1):
        temp = 0
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwaps = numSwaps + 1
    totalSwaps = totalSwaps + numSwaps
    if numSwaps == 0:
        break

firstElement = a[0]
lastElement = a[n-1]

print("Array is sorted in " + str(totalSwaps) + " swaps.")
print("First Element: "+str(firstElement))
print("Last Element: "+str(lastElement))
