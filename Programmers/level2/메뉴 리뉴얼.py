from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    orders.sort(key=len)

    for n in course:
        candidates = []
        for order in orders:
            for li in combinations(order,n):
                res = "".join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]



    return sorted(answer)