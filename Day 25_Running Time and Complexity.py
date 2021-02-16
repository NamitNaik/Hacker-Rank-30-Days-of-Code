# Enter your code here. Read input from STDIN. Print output to STDOUT
def isprime(i):
    if i <= 1:
        return False
    if i <= 3:
        return True
    if (i % 2 == 0 or i % 3 == 0):
        return False

    j = 5
    while(j * j <= i):
        if (i % j == 0 or i % (j + 2) == 0):
            return False
        j = j + 6
    return True


t = int(input())
n_list = list()

for i in range(t):
    n = int(input())
    n_list.append(n)

for i in n_list:
    if isprime(i) == True:
        print("Prime")
    else:
        print("Not prime")
