def solution(n):
    answer = 0
    n = list(str(n))
    sort_num = sorted(n, reverse = True)
    answer += int("".join(sort_num))
    return answer
