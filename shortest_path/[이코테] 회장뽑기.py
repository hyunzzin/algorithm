import sys
input = sys.stdin.readline
n = int(input())
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
while True:
    i, j = map(int, input().split())
    if i==-1 and j==-1: break
    graph[i][j] = 1
    graph[j][i] = 1

for k in range(n+1):
    for i in range(n+1):
        graph[i][i] = 0
        for j in range(n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
can = [0]
min_N = INF # 회장 후보 점수
for g in graph[1:]:
    max_N = max(g[1:])
    can.append(max_N)
    min_N = min(min_N, max_N)

result = []
for c in range(1,n+1):
    if can[c] == min_N:
        result.append(c)
        
print(min_N,len(result))
print(*result)
