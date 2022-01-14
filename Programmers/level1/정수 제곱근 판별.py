def solution(n):
    answer = 0
    if (n ** (1/2)).is_integer():
        answer += (n ** (1/2) + 1) ** 2
    else:
        answer += -1
    return answer

## is_integer()함수 : float값이 정수인지 확인하는 함수
