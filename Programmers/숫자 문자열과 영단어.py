def solution(s):
    answer = ""
    temp = ""
    a = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            for key, value in a.items():
                if key in temp:
                    answer += value
                    temp = ""
    
    answer = int(answer)
    
    return answer
    