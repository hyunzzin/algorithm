'''
잃어버린 괄호
숫자 사이사이에만 괄호 넣기 가능
일단 분리
'''
import sys
sen = sys.stdin.readline().strip('\n')
arr = []
num = ''
minus = False
for s in sen:
    if s.isdigit(): # 숫자면
        num+=s
    elif s == '+':
        arr.append(str(int(num)))
        arr.append(s)
        num = ''
    else: # 연산자면
        if minus: # 열려있으면 / 숫자 ) -
            arr.append(str(int(num)))
            arr.append(')')
            arr.append(s)
            num = ''
            arr.append('(')
        else: # 마이너스가 없었다면 / 숫자 - (
            arr.append(str(int(num)))
            arr.append(s)
            num = ''
            arr.append('(')
            minus = True
arr.append(str(int(num)))
if minus:
    arr.append(')')
print(eval(''.join(arr)))
