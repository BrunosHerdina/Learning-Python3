#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def IsPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return(False)
        return(True)
    else:
        return(False)
        
def getTotalX(a, b):
    poss=[]
    newa=a.copy()
    divided=0
    divisor=2
    mmc=1
    
    while sum(newa)!=len(newa):
        for x in range(len(newa)):
            if newa[x]%divisor==0:
                divided=1
                newa[x]//=divisor
        if divided==0:
            divisor+=1
            while not IsPrime(divisor):
                divisor+=1
        else:
            mmc*=divisor
        divided=0
        
    i=1
    while mmc*i<=b[0]:
        poss.append(mmc*i)
        i+=1
    pos=[]
    for i in b:
        for x in range(len(poss)):
            if i%poss[x]!=0:
                pos.append(x)
    pos=set(pos)
    return(len(poss)-len(pos))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
