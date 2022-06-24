from itertools import repeat
t = int(input())
while t>0:
    print(f"t = {t}")
    n,f = [int(x) for x in input().split()]
    data = []
    for _ in range(n):
        t,d = [int(x) for x in input().split()]
        data.extend(repeat(d,t))
    print(sum(data[f:]))
    t -= 1 