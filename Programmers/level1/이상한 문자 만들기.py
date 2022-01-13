def solution(s):
    answer = []
    s_list = list(map(list, (s.split(" ")))) # 리스트안에 리스트로 분리
    
    for words in s_list:
        for i in range(len(words)):
            if i % 2 == 0:
                words[i] = words[i].upper()
            else:
                words[i] = words[i].lower()
    
    for words in s_list:
        a = "".join(words)
        answer.append(a)
    
    return " ".join(answer)