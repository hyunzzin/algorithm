import sys
n = int(sys.stdin.readline())
result = [i for i in range(1,n+1)]
st = 0
while len(result)-st > 1:
    st+=1
    result.append(result[st])
    st+=1
print(result[st])
