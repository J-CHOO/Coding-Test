n = int(input())
p = list(map(int,input().split()))


result = [0,0]
temp = [9999999999999]

for i in range(len(p)):
        for j in range(i+1, len(p)):
            sum_p = abs(p[i] + p[j])
            
            if sum_p < temp[0]:
                temp[0] = sum_p
                result[0] = p[i]
                result[1] = p[j]

print(result[0], result[1])
