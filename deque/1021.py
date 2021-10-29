'''
1. 첫번째 원소를 뽑아낸다.
2. 왼쪽으로 한 칸 이동시킨다.
3. 오른쪽으로 한 칸 이동시킨다.
N : 큐에 처음 포함되어 있던 수 (N <= 50, 자연수)
M : 뽑아내려고 하는 수 (<= N, 자연수)
연산의 최솟값 구하기
'''
from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1,N+1)])
result = 0
for m in a:
    cnt = 0
    while deq[0] != m:
        cnt+=1
        deq.rotate(1)
    result += min(cnt, len(deq)-cnt)
    deq.popleft()
print(result)
            
    
