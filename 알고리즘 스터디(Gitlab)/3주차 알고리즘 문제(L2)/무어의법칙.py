n = int(input())

result = []

rec = str(2 ** n)

for i in range(len(rec)):
    result.append(int(rec[i]))

print(sum(result))
