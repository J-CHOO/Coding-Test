n = int(input())
h = list(map(int,input().split()))

count = n

for i in range(len(h)-1):
    for j in range(i+1, len(h)):
            if h[i] - h[j] == 1:
                count -= 1
                h[i] = 0
            else:
                pass
print(count)

#80점(5번 케이스 오답)
