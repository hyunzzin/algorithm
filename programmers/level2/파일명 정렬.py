def solution(files):
    ans = []
    '''
    처음 숫자가 나오는 부분까지 자르기
    '''
    # head, number, tail을 저장할 배열
    file = [[k for _ in range(3)]for k in range(len(files))]
    for i in range(len(files)):
        s = files[i]
        st = 0
        num = ''
        for k in range(2): # 세부분으로 나눠서 저장할 index
            for j in range(st,len(s)): # 문자열을 돌면서 자르기
                if k==0 and s[j].isdigit():
                    file[i][0] = s[:j].lower()
                    st = j
                    break
                elif k==1 and not s[j].isdigit():
                    break
                elif k==1:
                    num += s[j]
        file[i][1] = int(num)
    file.sort(key = lambda x: (x[0], x[1]))
    for i in file:
        ans.append(files[i[2]])
    return ans


