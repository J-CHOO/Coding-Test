n, k = map(int, input().split())

result = []

for i in range(1,n+1):
    result.append(i ** k)

print(sum(result) % 1000000009)
