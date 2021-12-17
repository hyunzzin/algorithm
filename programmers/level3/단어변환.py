'''
단어변환(30분)
BFS, 순회(visited 아닌거)해서 한글자만 다른 글자를 찾는다.
q에 집어넣기, visited true
[1,2,3,2,3,4]
'''
from collections import deque
# 한글자만 다른지 확인
def differ(x,w):
    cnt = 0
    for i in range(len(x)):
        if x[i] != w[i]:
            cnt+=1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    
    visited = [False for _ in range(len(words))]
    q = deque([(begin,0)])
    while q:
        x,y = q.popleft() # 단어, 인덱스
        if x == target:
            return y
        for i in range(len(words)):
            if not visited[i]:
                # x와 words[i]가 한글자만 다르다면
                if differ(x,words[i]):
                    visited[i]=y+1
                    q.append((words[i],y+1))
    return 0
