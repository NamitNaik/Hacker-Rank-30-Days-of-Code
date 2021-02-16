# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        bitwise_list = list()
        c = 2
        for a in range(n):
            if (a+1) == n:
                break
            for b in range(n-(a+1)):
                bitwise = (a+1) & (b+c)
                bitwise_list.append(bitwise)
            c = c + 1

        max_possible = 0

        for i in bitwise_list:
            if i > max_possible and i < k:
                max_possible = i

        print(max_possible)
