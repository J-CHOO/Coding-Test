'''
함수 processOrder를 구현하세요.
'''

class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQueue = []

    def push(self, n) :
        '''
        queue에 정수 n을 넣습니다.
        '''
        self.myQueue.append(n)

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1 : 
            return
        
        del self.myQueue[0]   #del을 쓰면 리스트의 인자를 삭제할 수 있다.

    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myQueue)

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size() == 0 :
            return 1
        else:
            return 0

    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1 :
            return -1
        
        return self.myQueue[0]

    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1
        return self.myQueue[-1]
        
class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, time, orders):
    normalIndex = normalQueue.front()
    vipIndex = vipQueue.front()
    
    if vipIndex == -1 :
        return normalQueue
    if normalQueue == -1 :
        return vipQueue
    
    #밀린작업이 둘다 없을때
    #더 빨리 오는걸 먼저 처리한다
    if time < orders[normalIndex].time and time < orders[vipIndex].time:
        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue
    
    #밀린작업이 normal에만 있는 경우
    if time >= orders[normalIndex].time and time < orders[vipIndex].time:
        return normalQueue
    
    #밀린작업이 vip에만 있는 경우
    if time >= orders[vipIndex].time and time < orders[normalIndex].time:
        return vipQueue
    
    #밀린작업이 둘다 있을때, 무조건 vip가 우선
    return vipQueue

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    '''

    result = []
    
    normalQueue = Queue()
    vipQueue = Queue()
    
    jobEndTime = 0
    curTime = -1
    
    for i in range(len(orders)) :
        curTime = orders[i].time
        
        if orders[i].vip == 0 :
            normalQueue.push(i)
        else:
            vipQueue.push(i)
            
            
        while jobEndTime <= curTime and not(normalQueue.empty() == 1 and vipQueue.empty() == 1) :
            
            #normal 또는 vip를 선택
            targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            
            #처리할 주문번호 가져온다
            index = targetQueue.front()
            
            #주문을 처리 = jobEndTIme을 증가시킨다.
            #jobEndTime이 order[index].time보다 큰 경우 : 주문이 밀려있어서 이전 작업을 끝내자마자 바로 다음 작업 시작
            #order[index].time이 jobEndTime보다 큰 경우 : 주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우
            #(다음 작업이 들어온 시점에 처리를 한다.)
            jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
            
            result.append(index + 1)
            targetQueue.pop()
    while not(normalQueue.empty() == 1 and vipQueue.empty() == 1) :
        #normal 또는 vip를 선택
            targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            
            #처리할 주문번호 가져온다
            index = targetQueue.front()
            
            #주문을 처리 = jobEndTIme을 증가시킨다.
            #jobEndTime이 order[index].time보다 큰 경우 : 주문이 밀려있어서 이전 작업을 끝내자마자 바로 다음 작업 시작
            #order[index].time이 jobEndTime보다 큰 경우 : 주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우
            #(다음 작업이 들어온 시점에 처리를 한다.)
            jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration
            
            result.append(index + 1)
            targetQueue.pop()
    

    return result
