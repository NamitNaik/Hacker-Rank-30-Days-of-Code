#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    lst = list()
    while n > 0:
        rem = int(n % 2)
        n = int(n / 2)
        lst.append(rem)

    l = len(lst)
    rev_list = list()
    for i in reversed(range(l)):
        rev_list.append(lst[i])

    cons_list = list()
    c = 0
    for i in rev_list:
        if i == 1:
            c = c + 1
        else:
            if c >= 1:
                cons_list.append(c)
                c = 0
    if c >= 1:
        cons_list.append(c)

    print(max(cons_list))
