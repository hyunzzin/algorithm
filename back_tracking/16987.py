'''
계란으로 계란치기

무게는 바뀌지만 내구도는 안바뀌니까 무게랑 내구도를 따로 저장하기

'''
import sys
n = int(sys.stdin.readline()) # 계란의 수
# 계란 내구도와 무게
d = []
w = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    d.append(a)
    w.append(b)

def bt(a,cnt, mx): # a번째 계란으로 다른 계란을 깬다.
    if a == n:
        mx = max(mx, cnt)
        return mx
    
    if d[a] <= 0 or cnt == n-1: # 나빼고 깨져있거나 a번 계란이 깨져있으면 넘어감
        mx = bt(a+1,cnt, mx)
        return mx

    for t in range(n):
        if t==a or d[t] <= 0:
            continue
        # 계란을 서로 부딪힌다.
        d[a] -= w[t]
        d[t] -= w[a]
        if d[a] <= 0:
            cnt+=1
        if d[t] <= 0:
            cnt+=1
        mx = bt(a+1, cnt, mx)
        if d[a] <= 0:
            cnt-=1
        if d[t] <= 0:
            cnt-=1
        d[a] += w[t]
        d[t] += w[a]
    return mx

print(bt(0,0,0))









