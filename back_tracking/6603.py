'''
로또
수 6개 고르기, 중복 X, 오름차순
함수 정의
    def(cnt, k)
base condition
    if cnt == 6:
        print()
        return
재귀 식
    def(cnt+1, i)
'''
import sys
def bt(cnt, k):
    if cnt == 6:
        print(' '.join(map(str, arr)))
        return
    for i in range(k,seq[0]+1):
        if not visited[i]:
            visited[i] = True
            arr[cnt] = seq[i]
            bt(cnt+1, i)
            visited[i] = False
    
while True:
    seq = list(map(int, sys.stdin.readline().split()))
    visited = [False for _ in range(seq[0]+1)]
    arr=[False for _ in range(6)]
    if seq[0] == 0:
        break

    bt(0,1)
    print()
