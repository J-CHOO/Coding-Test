def solution(numbers, hand):
    answer = ""
    key_pad = {
        1:[0,0], 2:[1,0], 3:[2,0],
        4:[0,1], 5:[1,1], 6:[2,1],
        7:[0,2], 8:[1,2], 9:[2,2],
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
            L_dis = abs(L_hand[0]-key_pad[num][0])+abs(L_hand[1]-key_pad[num][1])
            R_dis = abs(R_hand[0]-key_pad[num][0])+abs(R_hand[1]-key_pad[num][1])
            
            if L_dis < R_dis:
                answer += "L"
                L_hand = key_pad[num]
            elif L_dis > R_dis:
                answer += "R"
                R_hand = key_pad[num]
            else:
                if hand == "left":
                    answer += "L"
                    L_hand = key_pad[num]
                else:
                    answer += "R"
                    R_hand = key_pad[num]
            
    
    return answer