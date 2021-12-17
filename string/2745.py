import sys
input = sys.stdin.readline
n,b = map(str,input().split())
n = n[::-1]
'''
알파벳이면 -55하면 됨
'''
ans = 0
for i in range(len(n)):
    s = n[i]
    if not s.isdigit():
        s = ord(s)-55
    ans += int(s)*(int(b)**i)
print(ans)
