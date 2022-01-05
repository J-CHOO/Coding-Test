def solution(N, stages):
    answer = []
    len_stages = len(stages)
    score = [0] * N
    
    for i in range(1,N+1):
        if len_stages != 0:
            score[i-1] = stages.count(i) / len_stages
            len_stages -= stages.count(i)
        else:
            score[i-1] = 0
    
        
    for i in range(len(score)):
        answer.append(score.index(max(score))+1)
        score[score.index(max(score))] = -9999 # 리스트내의 max를 초기화하기 위해서 매우 작은값으로 넣었다.

    return answer