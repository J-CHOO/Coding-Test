def solution(strings, n):
    answer = []
    temps = []

    for string in strings:
        temps.append(string[n] + string)
        temps.sort()

    for temp in temps:
        answer.append(temp[1:])

    return answer
'''
def solution(strings, n):
    return sorted(strings,key = lambda x : (x[n], x))
딴사람 풀이
'''