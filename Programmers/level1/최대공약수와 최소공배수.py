def solution(n, m):
    answer = []
    
    for i in range(min(n,m),0,-1): # 최대공약수 구하기
        if m % i == 0 and n % i == 0:
            a = i
            break
    answer.append(a)
    
    answer.append((n * m) / a) # 두 수를 곱해서 최대공약수로 나누어 준 몫이 최소공배수
    
    return answer