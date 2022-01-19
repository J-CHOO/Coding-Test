def solution(x):
    list_x = list(map(int, list(str(x))))
    
    if x % sum(list_x) == 0:
        return True
    else:
        return False