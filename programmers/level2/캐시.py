def solution(cacheSize, cities):
    for c in range(len(cities)):
        cities[c] = cities[c].lower()
    #print(cities)
    q = [[-1,-1,''] for _ in range(cacheSize)]
    cur = 0
    ans = 0
    if cacheSize == 0:
        return 5*len(cities)
    for i in range(len(cities)):
        flag = False
        for j in range(len(q)):
            if q[j][2]== cities[i]:
                #print(q[j])
                q[j][0]+=1
                ans+=1
                flag = True
                q.sort(reverse=True)
                break
        if flag: continue
        q[-1] = [0,i,cities[i]] # 언급횟수, 들어간 순서, 숫자
        q.sort(reverse=True)
        ans+=5
        #print(q)
    return ans
