'''
TASK:
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    temp_ = 0
    count = 0 
    while n > 0:
        if n % 2 == 1:
            count += 1
            if count > temp_:
                temp_ = count
        else:
            count = 0
        
        n = n // 2
    print(temp_)
