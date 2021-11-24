'''
부분수열의 합
합이 S가 되는 부분수열 개수
원소가 n개인 집합에서 부분집합의 개수는 2^n
부분집합을 고르는 것과 동일한 상황, 공집합은 빼고 2^n-1개의 모든 부분수열에 대해 합이 S와 일치하는지 확인
각 원소는 선택 or 선택안함 두가지로 나뉜다.
'''
import sys
n, s = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

def bt(cur,sumN, cnt):
    if cur == n:
        if sumN == s:
            return cnt+1
        return cnt
    
    cnt = bt(cur+1, sumN,cnt) # 안더하는 경우
    cnt = bt(cur+1,sumN+seq[cur],cnt) # 더하는 경우
    return cnt
cnt = bt(0, 0, 0)
if s == 0:
    print(cnt-1)
else:
    print(cnt)
