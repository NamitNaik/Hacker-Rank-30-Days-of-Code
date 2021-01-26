# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
sl = list()

for i in range(t):
    s = input()
    sl.append(s)

for i in sl:
    l = len(i)
    es = ""
    os = ""
    for j in range(l):
        if j % 2 == 0:
            es = es + i[j]
        else:
            os = os + i[j]
    print(es + " " + os)
