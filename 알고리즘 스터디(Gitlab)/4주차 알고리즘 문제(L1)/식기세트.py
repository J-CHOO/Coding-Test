c, s, e = map(int, input().split())

c_set = c // 2

if c_set < s:              # 숫가락이 젓가락세트보다 많을때
    if s - c_set >= e:              #남는게 반납해야 할 갯수보다 크거나 같을때
        max_set = c_set
    else:                           #남는게 반납해야 할 갯수보다 작을때
        max_set = c_set - round((e - (s - c_set)) / 3)              #전체 만들수 있는 세트에서 반납할 갯수만큼 빼준다
elif c_set == s:           #숫가락과 젓가락세트 갯수가 같을때
    if s >= e:
        max_set = s-e
    else:
        max_set = round((c+s-e) / 3)

else:                      #젓가락세트가 숫가락보다 많을때
    if (c_set-s) >= e:
        max_set = s
    else:
        max_set = s- round((e - (c_set-s)*2) / 3)

print(max_set)
