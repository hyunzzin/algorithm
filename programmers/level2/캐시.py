from collections import deque
def solution(cacheSize, cities):
    for c in range(len(cities)):
        cities[c] = cities[c].lower()
    q = deque([])
    ans = 0
    if cacheSize == 0:
        return 5*len(cities)
    for i in range(len(cities)):
        flag = False
        for j in range(len(q)):
            if cities[i] == q[j]:
                q.remove(cities[i])
                q.append(cities[i])
                flag = True
                ans+=1
                break
        if flag: continue
        if len(q) !=cacheSize:
            q.append(cities[i])
            ans+=5
        else:
            q.popleft()
            q.append(cities[i])
            ans+=5
    return ans
