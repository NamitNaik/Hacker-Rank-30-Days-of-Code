#!/bin/python3

import math
import os
import random
import re
import sys


def solve(N):
    if (N % 2 == 0):
        if (N >= 2 and N <= 5):
            print("Not Weird")
        if (N >= 6 and N <= 20):
            print("Weird")
        if (N > 20):
            print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    N = int(input())

    y = solve(N)
