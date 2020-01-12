#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    lst=[]

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        res=re.search("^[a-z.]+@gmail.com$",emailID)
        if res:
            lst.append(firstName)
    lst.sort()
    for i in lst:
        print(i)

