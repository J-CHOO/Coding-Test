import datetime as d
def solution(a, b):
    answer = ""
    day = ["MON", "TUE","WED","THU","FRI", "SAT", "SUN"]
    
    answer += day[d.date(2016, a, b).weekday()]
    return answer


'''다른사람풀이

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

print(getDayName(5,24))
'''