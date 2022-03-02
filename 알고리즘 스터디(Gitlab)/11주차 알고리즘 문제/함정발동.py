h_list = []
count = 0

#h_list만들기
for i in range(8):
    for j in input().split():
        h_list.append(j)

#함정에 따른 카운트
for i in range(len(h_list)):
    for j in range(len(h_list[i])):
        if (i+1) % 2 == 1:      #홀수줄일때
            if (j+1) % 2 == 1 and h_list[i][j] == "H":      #홀수번째 함정이 있는 칸에 사람이 있을때
                count += 1
            else:
                pass
        else:       #짝수줄일때
            if (j+1) % 2 == 0 and h_list[i][j] == "H":      #짝수번째 함정이 있는 칸에 사람이 있을때
                count += 1
            else:
                pass
print(count)
