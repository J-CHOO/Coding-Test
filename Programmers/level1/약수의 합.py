def solution(n):
    n_list = [num for num in range(1,n+1) if n % num == 0]
    return sum(n_list)