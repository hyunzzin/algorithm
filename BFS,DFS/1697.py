'''
숨바꼭질
수빈이의 현재 위치 : 점 N
동생의 위치 : 점 K
수빈이만 움직임, +1 / -1 / *2

출력
    수빈이가 동생을 찾을 수 있는 가장 빠른 시간

1. 수빈이가 움직일 수 있는 거리만큼의 배열 생성
2. q의 첫번째에는 수빈이의 위치
    탈출조건
        만약 n==k 라면 동생의 위치이므로 반환한다.
3. q-1, q+1, q*2씩 하는데
    만약 subin[x]숫자가 0 이상이라면(이미 수빈이가 지나간 위치이므로) continue
    q가 배열의 범위를 넘어가도 continue
    q.append(x)
    subin[x] = subin[cur]+1
'''
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
subin = [-1 for _ in range(21)] # 0 <= N <= 100000  
subin[n] = 0
subin[k] = -2
q = deque([n])
if n == k:
    subin[k] = 0
while q:
    cur = q.popleft()
    if cur == k:
        print(subin[cur])
        break
    for x in (cur-1,cur+1,cur*2):
        if x < 0 or x > 20: continue
        if subin[x] >= 0: continue
        q.append(x)
        subin[x] = subin[cur] +1




















