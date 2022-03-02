n, t = map(int,input().split())

a = list(map(int,input().split()))

count = 0
ordertime = 0

for i in a:
    ordertime += i
    
    if t >= ordertime:
        count += 1
        
    else:
        break
print(count)
