'''
재현 : 잘못된 수를 부를 때마다 0을 외침, 최근에 재민이가 쓴 수를 지우게 시킴
재민 : 모든 수의 합을 알고 싶음

1<= K <= 100,000
k개의 수는 모두 정수(n)이며 0< n <1,000,000
'''
import sys
stack = [0 for _ in range(100000)]
k = int(sys.stdin.readline())
cnt = 0
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        cnt-=1
    else:
        stack[cnt] = n
        cnt+=1
print(sum(stack[:cnt]))

# 시간 : 3888ms로 오래걸린다
# pop, append는 O(1)
# 총 시간복잡도는 O(n)일 수 밖에 없다.....근데 왜?

import sys
k = int(sys.stdin.readline())
stack = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))

# 왜 sys.stdin.readline()이 훨씬 시간이 적게 걸리지
