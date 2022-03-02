n = int(input())

n_list = []

for i in range(1,n+1):      #1부터 n까지 n_list에 추가
    n_list.append(str(i))

num = (''.join(n_list))      #n_list의 숫자들을 이어서 num 변수에 저장

print(num.index(str(n))+1)  #num안에서 n이 처음 나오는 위치의 index를 찾아준다(index는 0부터 시작하므로 1을 더해준다.)
