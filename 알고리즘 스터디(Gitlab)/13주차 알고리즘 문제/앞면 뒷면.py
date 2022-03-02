#80점 시간초과
n = int(input())

card = [0] * n
count = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if j % i == 0:
            if card[j-1] == 0:
                card[j-1] = 1
            else:
                card[j-1] = 0
for c in card:
    if c == 1:
        count += 1
print(count)
