def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        elif i.islower():
            answer += chr((ord(i)-ord("a")+n) % 26 + ord("a")) 
        else:
            answer += chr((ord(i)-ord("A")+n) % 26 + ord("A")) 
    return answer

"""
chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수,
>>> chr(97) # 'a'
ord(c)는 문자의 아스키 코드 값을 돌려주는 함수입니다.
>>> ord('a') # 97
"""