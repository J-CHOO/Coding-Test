n = 10000 - int(input())

money = [1000, 100, 10, 1]
result = []

for i in money:
    a = n // i
    result.append(a)
    n = n % i
print(sum(result))
