#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n<=pow(10,6) and n>=1:

        lst = []
        count = 0
        prev = 0
        while n != 0:
            lst.append(n % 2)
            n //= 2
        for i in lst:
            if i == 1:
                count += 1
            else:
                if prev < count:
                    prev = count
                count = 0
        if prev > count:
            print(prev)
        else:
            print(count)

