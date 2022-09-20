## nx2 타일링

</br>

### 접근법
1. 점화식 : 메모이제이션 리스트 memo
    - memo[i] = memo[i-1]+memo[i-2]

</br>

### 구현

```python
import sys
input = sys.stdin.readline
n = int(input())
memo = [0 for _ in range(1001)]
def dp(n):
    memo[1] = 1
    memo[2] = 2
    for i in range(3,n+1):
        memo[i] = (memo[i-1]+memo[i-2])%10007

dp(n)
print(memo[n])
```