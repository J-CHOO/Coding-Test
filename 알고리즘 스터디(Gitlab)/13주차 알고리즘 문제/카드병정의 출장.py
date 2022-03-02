from itertools import combinations

n, m  = map(int, input().split())

card = []

for i in range (1, n+1):
    card.append(i)

for i in combinations(card, m):
    print(*i)
