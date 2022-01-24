def solution(record):
    answer = []
    record_list = []
    enter_dict = {}
    
    for a in record: # record_list 만들기
        a = list(a.split(" "))
        record_list.append(a)
        
    for a in record_list: # enter_dict 만들기
        if a[0] == "Enter":
            enter_dict[a[1]] = a[2]
        elif a[0] == "Change":
            enter_dict[a[1]] = a[2]
    
    for a in record_list: # enter_dict이용하여 최종 answer 넣어주기
        if a[0] == "Enter":
            answer.append(f"{enter_dict[a[1]]}님이 들어왔습니다.")
        elif a[0] == "Leave":
            answer.append(f"{enter_dict[a[1]]}님이 나갔습니다.")
    return answer