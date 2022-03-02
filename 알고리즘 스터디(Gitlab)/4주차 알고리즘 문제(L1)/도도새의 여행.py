r, c, k = map(int, input().split())

if k == 1:
    print(1)
else:
    print((r * c + 1) % 2)
