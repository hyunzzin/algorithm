import sys
N = sys.stdin.readline().strip('\n')
stick=[]
r = False
answer = 0
for n in N:
    if n == '(':
        if r:
            stick.append('(')
        else:
            r = True
    elif n == ')':
        if r:
            r = False
            answer+= len(stick)
        else:
            stick.pop()
            answer +=1
print(answer)
            
