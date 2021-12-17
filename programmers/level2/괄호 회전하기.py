from collections import deque
def check(s):
    arr = {'(':')','[':']','{':'}'}
    # 문자열 대칭 확인
    q = []
    for i in range(len(s)):
        if s[i] =='{' or s[i]=='(' or s[i]=='[':
            q.append(s[i])
        else:
            if q:
                if arr[q[-1]] == s[i]:
                    q.pop()
                else:
                    return False
            else:
                return False
    return True
    
def solution(s):
    '''
    괄호 종류 : {}, (), []
    1. 회전
    2. 문자열 대칭 확인
    '''
    s = deque(s)
    ans = 0
    # 회전
    if len(s)==1 or len(s)%2==1:
        return 0
    for _ in range(len(s)):
        if check(s):
            ans+=1
        s.append(s.popleft())
    
    return ans
