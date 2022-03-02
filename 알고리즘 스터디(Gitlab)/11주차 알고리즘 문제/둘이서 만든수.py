t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a_sum = 0
b_sum = 0
a_sum_list = []
b_sum_list = []

count = 0

for i in range(len(a)):
    a_sum += a[i]
    a_sum_list.append(a_sum)
    for j in range(i+1,len(a)):
        a_sum += a[j]
        a_sum_list.append(a_sum)
    a_sum = 0

for i in range(len(b)):
    b_sum += b[i]
    b_sum_list.append(b_sum)
    for j in range(i+1,len(b)):
        b_sum += b[j]
        b_sum_list.append(b_sum)
    b_sum = 0

for i in range(len(a_sum_list)):
    for j in range(len(b_sum_list)):
        if a_sum_list[i] + b_sum_list[j] == t:
            count += 1

print(count)

#이분 탐색이 아니라 그냥 전체를 다 구해서 더한거라 마지막 case에서 시간초과가 떠서 80점 나왔네요.
