import sys
input = sys.stdin.readline
n,b = map(int, input().split())
ans = ''
'''
15%8 = 7
1
'''
add = 0
while n>=b:
    add = n%b
    n //= b
    if add > 9:
        add = chr(add + 55)
    ans+=str(add)
if n > 9:
    n = chr(n + 55)
ans+=str(n)
print(ans[::-1])
