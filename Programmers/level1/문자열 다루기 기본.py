def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.islower() == True or s.isupper() == True:
            answer = False
        else:
            answer = True
    else:
        answer = False
    return answer