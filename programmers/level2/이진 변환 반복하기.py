def solution(s):
    '''
    0제거 -> 길이를 2진수로 변환 (1이될때까지)
    '''
    # 0제거
    cnt,zero = 0,0
    while s!= '1':
        cnt+=1 # 회차
        one = 0
        for i in range(len(s)):
            if s[i] == '0':
                zero+=1
            else:
                one+=1
        s=bin(one)[2:]
    return [cnt,zero]
