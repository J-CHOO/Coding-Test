#분할정복법 거듭제곱과 같은 문제

a, b, c = map(int, input().split())

# a를 b번 곱한 후 c로 나누기 
def cal(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        temp = cal(a, b // 2, c)
        return (temp * temp) % c 
    else:
        temp = cal(a, (b-1) // 2, c)
        return (temp * temp * a) % c


print(cal(a, b, c))

