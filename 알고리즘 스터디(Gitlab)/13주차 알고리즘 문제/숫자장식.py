from itertools import product

n,m = map(int, input().split())

deco = []

for i in range(1, n+1):
    deco.append(i)

for i in product(deco, repeat=m):
    print(*i)
