def solution(name):
    # 첫번째가 아닌 A이상의 알파벳의 index 구하기
    
    front,back,start,end = 0,0,0,0
    for n in range(1,len(name)):
        if name[n] != 'A':
            back = len(name)-n
            break
    for n in range(len(name)-1,0,-1):
        if name[n] != 'A':
            front = n
            break
    for n in range(len(name)//2,len(name)):
        if name[n] != 'A':
            end = len(name)-n
            break
    for n in range(len(name)//2-1,-1,-1):
        if name[n] != 'A':
            start = n
            break
    
    add = min(start,end)*2 + max(start,end)
    ans = min(front, back,add)
    
    # 알파벳을 순회하면서 ord('A')의 값을 빼준거랑 그 값에서 -24한 절댓값이랑 더 작은거 더하기.
    for i in name:
        s = ord(i)-ord('A')
        ans+=min(s,abs(s-26))
    return ans
