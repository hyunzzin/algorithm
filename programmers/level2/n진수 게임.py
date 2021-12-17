def solution(n, t, m, p):
    arr = []
    ans = ''
    '''
    문자열을 먼저 만들어서 m만큼 띄워서 뽑는다. p-1부터 m간격으로 t*2까지
    list해서 extend
    10 + 55 -> chr 하면 A
    나머지부터 삽입
    '''
    start = 0
    while len(arr) < t*m:
        arr.extend(list(change(start,n)))
        start +=1
    for i in range(p-1,t*m,m):
        ans+=arr[i]
    
    return ans

# 진수변환
def change(num,b):
    s = ''
    while num >= b:
        first = num%b
        num = num//b
        if first > 9:
            first = chr(first+55)
        s = str(first)+s
    if num > 9:
        num = chr(num+55)
    s = str(num)+s
    return s
