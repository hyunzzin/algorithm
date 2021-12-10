import copy
from collections import deque
def solution(bridge_length, weight, truck_weights):
    tw = 0
    cnt = 1
    cur_i = 0
    bridge = [0 for _ in range(len(truck_weights))]
    truck = deque(copy.deepcopy(truck_weights))
    while True:
        if bridge[-1] == -1:
            return cnt
        
        # 트럭 입장
        if truck:
            if tw + truck[0] <= weight:
                tw += truck.popleft()
                cur_i += 1
        # 내보내는 동시에 들여와야 함
        for j in range(cur_i):
            # 다리 건너기
            if bridge[j] != -1: 
                bridge[j] +=1
            # 다리 마지막 도달 시 -1 넣기
            if bridge[j] == bridge_length:
                tw -= truck_weights[j]
                bridge[j] = -1
            
        cnt+=1
