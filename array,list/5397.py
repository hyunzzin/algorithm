'''
백스페이스 - (지우기)
화살표 < > - (커서 옮기기)
나머지 비밀번호의 일부
스택 2개로 구현하기
'''
n = int(input())
for _ in range(n):
    st1 = []
    st2 = []
    key = input()
    for k in key:
        if k == '-':
            if st1:
                st1.pop()
        elif k == '<':
            if st1:
                st2.append(st1.pop())
        elif k == '>':
            if st2:
                st1.append(st2.pop())
        else:
            st1.append(k)
    print(''.join(st1)+''.join(reversed(st2)))
