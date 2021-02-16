#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())

    gmail_users = list()

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if "@gmail" in emailID:
            gmail_users.append(firstName)

    gmail_users.sort()

    for firstname in gmail_users:
        print(firstname)
