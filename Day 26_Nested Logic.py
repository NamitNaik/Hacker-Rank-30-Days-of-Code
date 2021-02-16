# Enter your code here. Read input from STDIN. Print output to STDOUT
date_return = list(map(int, input().split()))
date_due = list(map(int, input().split()))


if date_return[2] < date_due[2]:
    fine = 0
elif date_return[2] > date_due[2]:
    fine = 10000
elif date_return[1] > date_due[1]:
    fine = 500 * (date_return[1]-date_due[1])
elif date_return[0] > date_due[0]:
    fine = 15 * (date_return[0]-date_due[0])
else:
    fine = 0

print(fine)
