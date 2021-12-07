from collections import deque
import math,copy
def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        q.append(math.ceil((100-progresses[i])/speeds[i]))
    ans = []
    print(q)
    days = 0
    while q:
        days += (q.popleft()-days)
        cnt = 1
        q_copy = copy.deepcopy(q)
        while q:
            if q[0] <= days:
                q.popleft()
                cnt+=1
            else:
                break
        ans.append(cnt)     
        
    return ans
