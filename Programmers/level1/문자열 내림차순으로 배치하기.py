def solution(s):
    lower_list = []
    upper_list = []
    lower = ''
    upper = ''
    for a in s:
        if a.isupper() == False:
            lower_list.append(a)
        else:
            upper_list.append(a)
            
    lower_list.sort()
    upper_list.sort()
    
    for b in reversed(lower_list):
        lower += b
    for c in reversed(upper_list):
        upper += c
    return lower + upper