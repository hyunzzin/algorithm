def solution(record):
    answer = []
    data = {}
    for r in record:
        r_arr = r.split(' ')
        if r_arr[0] == 'Enter':
            answer.append((r_arr[1], 1))
            data[r_arr[1]] = r_arr[2]
        elif r_arr[0] == 'Change':
            data[r_arr[1]] = r_arr[2]
        elif r_arr[0] == 'Leave':
            answer.append((r_arr[1], 2))
    for i in range(len(answer)):
        if answer[i][1] == 1: # enter
            answer[i] = data[answer[i][0]] + '님이 들어왔습니다.'
        else: # leave
            answer[i] = data[answer[i][0]] + '님이 나갔습니다.'
    return answer
