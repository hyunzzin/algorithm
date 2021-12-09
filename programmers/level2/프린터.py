import copy
from collections import deque
def solution(priorities, location):
    cnt = 1
    p = sorted(copy.deepcopy(priorities))
    priorities = deque(priorities)
    target = p.pop()
    print(target)
    while True:
        if target == priorities[0]:
            if location == 0:
                return cnt
            else:
                priorities.popleft()
                target = p.pop()
                cnt+=1
        else:
            priorities.append(priorities.popleft())
        if location == 0:
            location = len(priorities)-1
        else:
            location -=1
    
