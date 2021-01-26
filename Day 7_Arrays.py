#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rev_string = ""
    for i in range(n):
        rev_string = str(arr[i]) + " " + rev_string
    print(rev_string)
