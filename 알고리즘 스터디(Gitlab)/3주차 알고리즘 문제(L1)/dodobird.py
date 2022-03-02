N = int(input())
B = list(map(int, input().split()))

list_a = []
cnt = 1

for i in range(len(B)):
    list_a.append((cnt * B[i]) - sum(list_a))
    cnt += 1

print(*list_a)

# for i in list_a:
#     print(i,end = " ") 이렇게도 리스트 출력가능
