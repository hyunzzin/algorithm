'''
로프
k개의 로프, 중량이 w
로프를 이용하여 들어올릴 수 있는 물체의 최대 중량
'''
import sys
N = int(sys.stdin.readline())
weight = [int(sys.stdin.readline()) for _ in range(N)]
weight.sort()
result = 0
for w in range(N):
    result = max(result, weight[w]*(N-w))
print(result)
