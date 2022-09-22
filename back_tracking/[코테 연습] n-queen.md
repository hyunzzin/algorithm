## N-Queen

</br>

### 접근법
좌우, 상하, 대각선 모든 방향으로 이동이 가능하다

1. 한 줄에 한개 밖에 못놓음

2. 바로 위의 대각선만 신경써도 된다.

위에 놓은 퀸의 x,y에서 (x+1, y-1), (x+1, y+1)에는 놓을 수 없다.

3. 이미 놓은 퀸과 동일한 y 좌표에도 놓을 수 없다.

4. stack에다가 넣기

</br>

### 구현

```python
import sys
input = sys.stdin.readline
n = int(input()) # queen 개수 입력받기



chess = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
visited = [False for _ in range(n)]

stack = []
def bt(st):
    # 퀸의 개수가 채워지면 탈출
    if len(stack) == n:
        global cnt
        cnt+= 1
        return

    for i in range(n):
        flag = True
        if visited[i] == True: continue
        if stack:
            for s in stack:
                x, y = s
                if i == y-(st-x) or i == y+(st-x):
                    flag = False
        if not flag: continue
        visited[i]=True
        stack.append((st,i))
        bt(st+1)
        stack.pop()
        visited[i] = False
bt(0)
print(cnt)
```


