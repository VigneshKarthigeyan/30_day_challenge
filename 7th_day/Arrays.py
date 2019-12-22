#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n>=1 and n<=1000:
        arr = list(map(int, input().rstrip().split()))
        arr.reverse()
        for i in arr:
            if i >= 1 and i <= 10000:
                print(i,end=" ")
