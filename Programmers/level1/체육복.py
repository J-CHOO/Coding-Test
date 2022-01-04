def solution(n, lost, reserve):
    answer = 0
    lost.sort() #test case n: 4 [4, 2] [3, 5]에서 처럼 오름차순이 되어있지 않은 리스트를 sort로 정렬한다.
    reserve.sort()
    lost_set = set(lost) - set(reserve) #set함수로 집합으로 만든후 차집합으로 중복되어 있는 교집합부분을 빼준다.
    reserve_set = set(reserve) - set(lost)
    
    for num in reserve_set:
        if num not in lost_set:
            if num - 1 in lost_set:
                lost_set.remove(num - 1)
            elif num + 1 in lost_set:
                lost_set.remove(num + 1)
        else:
            lost_set.remove(num)
    
    answer += n - len(lost_set)
    
    return answer