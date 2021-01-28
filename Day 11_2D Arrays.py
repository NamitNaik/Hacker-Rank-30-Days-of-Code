#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    i = 0
    j = 0
    lst = list()
    for k in range(4):
        if k != 0:
            i = i + 1
            j = 0
        for l in range(4):
            sa = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1] + \
                arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            lst.append(sa)
            j = j+1

    print(max(lst))
