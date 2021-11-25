'''
N과 M(9)
함수 정의
    def(cnt)
base condition
    if cnt == m:
        print()
        return
재귀 식
    def(cnt+1)

'''
import sys
n,m = map(int, sys.stdin.readline().split())
seq = sorted(list(map(int, sys.stdin.readline().split())))
visited_n=[False for _ in range(n)]
arr = [False for _ in range(m)]
def bt(cnt):
    if cnt == m:
        print(' '.join(map(str,arr)))
        return
    visited = 0
    for i in range(n):
        if visited!=seq[i] and not visited_n[i]:
            visited = seq[i]
            visited_n[i] = True
            arr[cnt] = seq[i]
            bt(cnt+1)
            visited_n[i] = False

bt(0)
