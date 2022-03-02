n = int(input())
result = []

for i in range(n):
    d = int(input())
    result.append(d)
result = sum(result)

print(str(result)[:10])
