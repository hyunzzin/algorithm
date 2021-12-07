import math
seq = ['1','2','4']
s_cnt = 0
def bt(s, cnt, z,arr): # s는 몇번째 수인지, 번째 수가, z는 자릿수
    global s_cnt
    if cnt == z:
        s_cnt+=1
        return
    for i in range(3):
        arr[cnt]=seq[i]
        bt(s, cnt+1, z,arr)
        if s == s_cnt:
            return
    
    
def solution(n):
    global sumN
    z = math.floor(math.log((n*2)/3+1, 3))
    s = n - (3**(z+1)-3)/2
    if s == 0:
        return '4'*z
    arr = [0 for _ in range(z+1)]
    bt(s, 0,z+1,arr)
    return ''.join(arr)

print(solution(3))

