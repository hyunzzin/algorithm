import sys
n = int(input())
for _ in range(n):
    arr = [0 for _ in range(26)]
    aw,bw = map(str,sys.stdin.readline().split())
    if len(aw) != len(bw):
        print('Impossible')
        continue
    for a in aw:
        arr[ord(a)-97]+=1
    cnt=len(aw)
    for b in bw:
        if arr[ord(b)-97]>0:
            cnt-=1
            arr[ord(b)-97]-=1
    if cnt==0:
        print('Possible')
    else:
        print('Impossible')
        
