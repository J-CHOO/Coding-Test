n = int(input())
result = []

for i in range(1, n):
    if i % 3 == 0:
        result.append(i)
    elif i % 5 == 0:
        result.append(i)
print(sum(result))
