def solution(arr, divisor):
    answer = []
    for num in arr[:]:
        if num % divisor == 0:
            answer.append(num)
        else:
            arr.remove(num)
        if len(arr) == 0:
            answer.append(-1)
    answer.sort()
    return answer

"""
그냥 for num in arr:로 했을때는 arr에 있는 원소가 다 지워지지 않았었다.
그 이유는, arr = [3, 2, 6]일때 인덱스가 0인 3을 먼저 지우고 나면 그다음 인덱스가 1이 되어 버리는데
그러면 arr = [2, 6]이 되어 2를 건너뛰고 인덱스가 1인 6을 지워버리므로 [2]가 남아 버리게 된다.
이를 위해서는 리스트를 카피하는 방식으로 arr[:]로 for문을 돌면 원본데이터를 해치지 않고 리스트에 있는
원소를 제대로 제거할 수 있게 된다.

"""