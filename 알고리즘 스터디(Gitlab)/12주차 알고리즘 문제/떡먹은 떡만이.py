m = int(input())

temp = 1

for i in range(m):
    x, y = list(map(int, input().split()))
    
    if temp == x:
        temp = y
    elif temp == y:
        temp = x
print(temp)
