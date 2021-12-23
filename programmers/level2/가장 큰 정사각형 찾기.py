def solution(board):    
    cn = len(board)
    rn = len(board[0])
    '''
    (i,j)위치에서 가능한 사각형의 최대 길이는 min((i-1,j-1)에서 최대 길이,(i-1,j)에서 최대 길이,(i,j-1)에서 최대 길이)+1임을 이용
    0 1 1 1     0 1 1 1
    1 1 1 1     1 1 2 2
    1 1 1 1     1 2 2 3
    0 0 1 0     0 0 1 0
    
    1 1 0   1 1 0
    1 0 1   1 0 1
    0 1 1   0 1 1
    '''
    maxN = 0
    for i in range(cn):
        up,dia,left = 0,0,0
        for j in range(rn):
            if board[i][j] ==1:
                if i-1>=0 and j-1>=0:
                    dia = (i-1,j-1)
                    up = (i-1,j)
                    left = (i,j-1)
                    board[i][j] = min(board[up[0]][up[1]],board[left[0]][left[1]],board[dia[0]][dia[1]])+1
                
                maxN = max(maxN,board[i][j])
    return maxN**2
