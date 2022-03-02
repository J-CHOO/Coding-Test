import math

n,s = map(int, input().split())
p = list(map(int, input().split()))

left = 0
right = 0
temp_sum = 0
cnt = math.inf

while True:
    if temp_sum >= s :
        cnt = min(cnt, right - left)
        temp_sum -= p[left]
        left += 1
    
    elif right == n:
        break
    
    else:
        temp_sum += p[right]
        right += 1

if cnt == math.inf:
    print(0)
else:
    print(cnt)

