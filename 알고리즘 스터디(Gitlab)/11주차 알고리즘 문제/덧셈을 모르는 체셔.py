n = int(input())

str_n = str(n)

if len(str_n) == 2:
    result = int(str_n[0]) + int(str_n[1])
elif len(str_n) == 3:       #3개면 10이 무조건 하나는 들어가 있음
    result = 10 + int(str_n.replace("10",""))
else:       #4개면 무조건 10,10
    result = 10 + 10

print(result)
