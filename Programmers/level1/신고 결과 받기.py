def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    rep_dict = {id : [] for id in id_list}
    
    for i in report:
        a,b = i.split(" ")
        rep_dict[b].append(a)
    
    for key, value in rep_dict.items():
        if len(value) >= k:
            for a in value:
                answer[id_list.index(a)] += 1
    return answer

    '''
    실패한 코드

    def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ban = []
    report = set(report)
    rep_dict = {id : [] for id in id_list}
    ban_set = []
    
    for i in report:
        a,b = i.split(" ")
        rep_dict[a].append(b)
        ban.append(b)
    
    for i in ban:
        if ban.count(i) >= k:
            ban_set.append(i)
    ban_set = set(ban_set)
    
    for key, value in rep_dict.items():
        for s in ban_set:
            if s in value:
                answer[id_list.index(key)] += 1
    return answer
    '''