#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    for i in range(11):
        if i == 0:
            continue
        p = n * i
        print(str(n) + ' x ' + str(i) + ' = ' + str(p))
