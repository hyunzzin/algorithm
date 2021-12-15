def bfs(computers,i,visited):
    visited[i] = True
    for j in range(len(computers[i])):
        if computers[i][j] and not visited[j] and i!=j:
                   bfs(computers, j, visited)
    return

def solution(n, computers):
    ans = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(computers,i,visited)
            ans+=1
    return ans
