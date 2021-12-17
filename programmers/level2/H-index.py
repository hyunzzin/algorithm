def solution(citations):
    '''
    5편 중 3번 이상 인용된 논문이 3편이상이고 나머지 논문이 3번 이하
    중간 값을 찾아야 함
    0, 1, 3, 5, 6
    arr[1,1,0,1,0,1,1] # 뒤의 숫자 합보다 index가 작으면 멈춤
    '''
    arr = [0 for _ in range(10001)]
    maxN,sumN,ans = 0,0,0
    for i in citations:
        arr[i]+=1
        maxN = max(maxN, i)
    for j in range(maxN,-1,-1):
        if sumN > j:
            break
        sumN+= arr[j]
        ans = j
    return ans
