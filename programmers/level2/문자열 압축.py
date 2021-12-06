import sys
def solution(s):
    result = sys.maxsize
    if len(s) == 1:
        return 1
    for n in range(1, (len(s)//2)+1): # 문자 단위 
        com = s[:n]
        cnt = 1
        ans = ''
        for st in range(n,len(s),n): # 문자 단위만큼의 반복문
            if com == s[st:st+n]: # 다음 부분이 같은 경우
                cnt+=1
            else: # 다음 부분이 같지 않으면
                if cnt != 1:
                    ans = ans + str(cnt) + com
                else:
                    ans = ans + com
                com = s[st:st+n]
                cnt = 1
        if cnt != 1:
            ans = ans + str(cnt) + com
        else:
            ans = ans + com
        result = min(result, len(ans))
    
    return result
