'''
카드 구매하기
민규가 N개의 카드를 갖기 위해 지불해야 하는 금액의 최댓값
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
memo = [0 for _ in range(N+1)]
def card(N):
    if N == 1:
        return
    for i in range(1,N+1):
        sumN  = arr[0]
        for j in range(i//2+1):
            temp = memo[j]+memo[i-j]
            if j == 0:
                temp = arr[i-1]
            sumN = max(sumN, temp)
        memo[i] = sumN
    print(memo[-1])
    
card(N)
