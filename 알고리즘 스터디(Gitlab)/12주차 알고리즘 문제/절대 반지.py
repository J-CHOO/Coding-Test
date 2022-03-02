nickname = str(input())
n = int(input())

count = 0

for i in range(n):
    ring = input()
    ring += ring
    if nickname in ring:
        count += 1
print(count)
