#!/bin/python3

import sys


S = input().strip()

try:
    I = int(S)
    print(I)
except ValueError:
    print("Bad String")
