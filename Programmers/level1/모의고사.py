def solution(answers):
    num_1 = [1, 2, 3, 4 ,5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == num_1[i % 5]:
            score[0] += 1
        if answers[i] == num_2[i % 8]:
            score[1] += 1
        if answers[i] == num_3[i % 10]:
            score[2] += 1
    for i, j in enumerate(score): #enumerate함수는 리스트의 해당원소의 인덱스를 튜플로 반환해준다.
        if j == max(score): 
            answer.append(i+1)

    return answer