# 완전탐색
def search(n,l,dungeons,visited,q,k,cnt):
    if n==l:
        cnt = q.count(1)
        return cnt
    for i in range(l):
        if not visited[i]:
            visited[i] = True
            if k >= dungeons[i][0]:
                q[n] = 1
                cnt = max(cnt,search(n+1,l,dungeons,visited,q,k-dungeons[i][1],cnt))
                q[n] = 0
            else:
                cnt = max(cnt,search(n+1,l,dungeons,visited,q,k,cnt))
            visited[i] = False
    return cnt

def solution(k, dungeons):
    '''
    최소 필요 피로도 >= 소모 피로도 1이상 1000이하
    유저가 갈 수 있는 최대 던전 수
    '''
    len_d = len(dungeons)
    # 완탐?
    visited = [False for _ in range(len_d)]
    q= [0 for _ in range(len_d)]
    return search(0,len_d,dungeons,visited,q,k,0)
