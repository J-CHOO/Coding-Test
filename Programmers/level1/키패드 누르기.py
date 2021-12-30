def solution(numbers, hand):
    key_pad = {
        1:[0,0], 2:[1,0], 3:[2,0]
        4:[0,1], 5:[1,1], 6:[2,1]
        7:[0,2], 8:[1,2], 9:[2,2]
        "*":[0,3], 0:[1,3], "#":[2,3]}
    L_hand = key_pad["*"]
    R_hand = key_pad["#"]
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            L_hand = key_pad[num]
        elif num in [3, 6, 9]:
            answer += "R"
            R_hand = key_pad[num]
        else:
            pass

            
    print(answer)
    return answer