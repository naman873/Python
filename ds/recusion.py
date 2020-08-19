def mze(board,c_r,c_c,t_r,t_c,row,col,hell):
    if c_c==t_c and c_r==t_r:
        print(hell)
        return

    if (c_r not in range(0,row)) or (c_c not in (0,col)):
        return

    if board[c_r][c_c]:
        return

    board[c_r][c_c]=True
    mze(board,c_r-1,c_c,t_r,t_c,row,col,hell+"U")
    mze(board, c_r +1,c_c , t_r, t_c, row, col, hell + "D")
    mze(board, c_r,c_c +1 , t_r, t_c, row, col, hell + "R")
    mze(board, c_r,c_c -1, t_r, t_c, row, col, hell + "L")
    board[c_r][c_c]=False

board=[[False]*5 for i in range(3)]
print(mze(board,0,0,2,2,3,5,""))