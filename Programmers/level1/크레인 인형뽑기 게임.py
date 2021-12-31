def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                if len(basket) == 0:
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0
                else:
                    if basket[-1] == board[j][i-1]:
                        basket.pop()
                        board[j][i-1] = 0
                        answer += 2
                    else:
                        basket.append(board[j][i-1])
                        board[j][i-1] = 0
                break                 
            
    return answer
#break를 안걸어줘서 board[j][i-1]에 있는 원소를 전부 끝까지 basket에 추가했어서 계속 답이 안나왔었음