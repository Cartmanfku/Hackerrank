#!/bin/python

# Complete the function below.
import math

def oct2bin(n):
    return bin(n)[2:] #bin() returns '0bxxxxx',remove first 2 chars

"""
maxXor is O(n) where n is bit length of R
"""
def  maxXor( l,  r):
    L = oct2bin(l)
    R = oct2bin(r)
    lenL = len(L)
    lenR = len(R)

    if lenR > lenL:
        """
        if lenR > lenL, then the biggest bit is 1 for R and 0 for L.
        in this case, maxXor of L <= A <= B <= R is 2^lenR - 1.
        you can think about this case:
        L 01111
        R 10000
        """
        return int(math.pow(2,lenR)) -1
    else:
        """
        else find out on which bit, R is 1 and L is 0.
        we recurse to that case and starts on that bit.
        anything else is same as above case.
        """
        for i in range(1, lenR):
            if L[i] == R[i]:
                continue
            else:
                return int(math.pow(2,lenR-i)) - 1
            
   

_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
