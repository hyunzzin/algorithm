'''
트럭
programmers 다리를 지나는 트럭과 유사
n개의 트럭 중 w대의 트럭이 동시에 올라갈 수 있다.
트럭의 무게의 합은 L이하
'''
import sys,copy
from collections import deque
input = sys.stdin.readline
n,w,L = map(int, input().split()) # 트럭 수, 다리길이, 최대하중

truck = list(map(int, input().split()))
ctruck = deque(copy.deepcopy(truck))
brid = [0 for _ in range(n)] # 트럭 개수
cnt = 0
cur_w = 0
st,ed = 0,0
while st!=n:
    # 트럭 입장
    if ctruck:
        if cur_w+ ctruck[0] <= L:
            cur_w+=ctruck.popleft()
            ed+=1
    # 트럭 지나가기
    for b in range(st,ed):
        brid[b]+=1
    if brid[st]==w:
        cur_w-= truck[st]
        st+=1
    cnt+=1
print(cnt+1)    
