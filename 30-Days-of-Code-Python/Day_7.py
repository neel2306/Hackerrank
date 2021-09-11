'''
TASK:
Given an array, A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.
'''
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(str, input().rstrip().split()))
    rev_arr = arr[::-1]
    rev_arr1 = " ".join(rev_arr)
    print(rev_arr1)
