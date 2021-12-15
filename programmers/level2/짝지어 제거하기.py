def solution(s):
    if len(s)==1:
        return 0
    arr = list(s)
    ans = [] # 대기 배열
    tmp = arr[0] # 비교수
    for i in range(1,len(arr)):
        if tmp: # 비교수가 있으면
            if tmp == arr[i]: # 비교수와 같으면 제거
                tmp = 0
                if ans: # 하지만 대기 배열이 있으면 대기 배열 숫자 추가
                    tmp = ans.pop()
            else: # 비교수와 다르면
                ans.append(tmp)
                tmp = arr[i]
        else: # 비교수가 없으면
            tmp = arr[i] # 비교할 숫자에 추가한다.
        if i == (len(arr)-1):
            ans.append(tmp)
    if ans and tmp:
        return 0
    return 1
