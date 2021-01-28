# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
Dict = {}

for i in range(n):
    data = input().split(' ')
    Dict[data[0]] = data[1]

sl = list()

while True:
    try:
        name = input()
        if name in Dict:
            pn = Dict.get(name)
            st = name + "=" + pn
            sl.append(st)
        else:
            st = "Not found"
            sl.append(st)
    except EOFError:
        break

for i in sl:
    print(i)
