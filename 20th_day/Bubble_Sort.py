#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count=0
# Write Your Code Here
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            count+=1
            a[j],a[j+1]=a[j+1],a[j]
print("Array is sorted in %d swaps."%count)
print("First Element: %d"%a[0])
print("Last Element: %d"%a[n-1])
