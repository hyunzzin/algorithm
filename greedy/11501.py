'''
주식
하나를 산다
다 판다
아무것도 안한다
거꾸로 계산하기
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    result = 0
    sell = 0
    for i in range(N-1, -1,-1):
        if sell < arr[i]: # 파는 날
            sell = arr[i]
        else: # 사는 날
            result += sell-arr[i]
    print(result)
            
